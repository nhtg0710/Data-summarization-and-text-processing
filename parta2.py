import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('plot1')
parser.add_argument('plot2')
args = parser.parse_args()

df = pd.read_csv('owid-covid-data-2020-monthly.csv')

# taking the final month of 2020 for each country
end_year = df.groupby('location').last()[['total_cases', 'total_deaths']]
end_year['final_fatality_rate'] = end_year['total_deaths']/end_year['total_cases']

# only calculate non na values for the plot
end_year = end_year.loc[end_year['final_fatality_rate'].notna()]

plt.scatter(end_year['total_cases'], end_year['final_fatality_rate'])
plt.xlabel('Cases')
plt.ylabel('Case fatality rate')
plt.title('Case fatality and total number of cases')
plt.grid(True)
plt.savefig(args.plot1)

plt.scatter(end_year['total_cases'], end_year['final_fatality_rate'])
plt.xscale("log")
plt.xlabel('Cases')
plt.ylabel('Case fatality rate')
plt.title('Case fatality and total number of cases (log scale)')
plt.grid(True)
plt.savefig(args.plot2) 