## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from IPython.display import display
from porter import porter

ps = nltk.PorterStemmer()

current_path = os.getcwd()
path = os.path.abspath("cricket")
os.chdir(path)

keyword_list = sys.argv[1:]
keyword_file = []

file_list = sorted(list(filter(os.path.isfile, os.listdir(path))))

for filename in file_list:
    content = ' '.join(porter(filename))
    has_keyword = True
    for word in keyword_list:
        if ps.stem(word) not in content: 
            has_keyword = False
    if has_keyword:
        keyword_file.append(filename)

os.chdir(current_path)
Document_ID = pd.read_csv('partb1.csv')
print(list(Document_ID.loc[Document_ID['filename'].isin(keyword_file)]['Document ID'].values))