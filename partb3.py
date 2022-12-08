## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os
from prep import preprocess
from IPython.display import display

current_path = os.getcwd()
keyword_list = sys.argv[1:]
path = os.path.abspath("cricket")
os.chdir(path)
keyword_file = []

file_list = sorted(list(filter(os.path.isfile, os.listdir(path))))
for filename in file_list:
    content = preprocess(filename).split()
    has_keyword = True
    for word in keyword_list:
        if word not in content:
            has_keyword = False 
    if has_keyword:
        keyword_file.append(filename)

os.chdir(current_path)
Document_ID = pd.read_csv('partb1.csv')
print(list(Document_ID.loc[Document_ID['filename'].isin(keyword_file)]['Document ID'].values))