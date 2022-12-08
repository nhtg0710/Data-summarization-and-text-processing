import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

# sum_if_nan helps deal with nan values when summing along a column
def sum_if_nan(series):
    if pd.isna(series).all():
        return np.NaN
    else:
        return series.sum()

covid_df = pd.read_csv('owid-covid-data.csv', encoding = 'iso-8859-1')

# only taking fields with values
covid_df = covid_df.iloc[:,0:16] 

# breaking date down into its components
covid_df['date'] = pd.to_datetime(covid_df['date'])
covid_df['month'] = covid_df['date'].dt.month
covid_df['year'] = covid_df['date'].dt.year

# collecting only data in year 2020 and in desired columns
covid_df_2020 = covid_df.loc[covid_df['year'] == 2020,['location','month','total_cases','new_cases','total_deaths','new_deaths']]

covid_2020_stat = covid_df_2020.groupby(['location','month']).agg({'total_cases':'last', 'new_cases': sum_if_nan, 'total_deaths': 'last', 'new_deaths': sum_if_nan})

# new column added: case fatality rate
covid_2020_stat['case_fatality_rate'] = covid_2020_stat['new_deaths'] / covid_2020_stat['new_cases']
covid_2020_stat = covid_2020_stat[['case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]
covid_2020_stat = covid_2020_stat.sort_values(by=['location','month'])

print(covid_2020_stat.head(5))
covid_2020_stat.to_csv(args.file) 