## Part B Task 1
import re
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

re.DOTALL
current_path = os.getcwd()
pattern = r'[A-Z]{4}\-\d{3}.{0,2}'
path = os.path.abspath("cricket")
fileID = []
os.chdir(path)
file_list = sorted(list(filter(os.path.isfile, os.listdir(path))))
for filename in file_list:
    if filename.endswith(".txt"):
        with open(filename, 'r') as f:
            content = f.read()
            result = re.search(pattern, content) 
            if len(result[0]) == 8:
                fileID.append(result[0])
            
            # if there is no spacing between doc ID and next word
            elif len(result[0]) == 9:
                if result[0][-1].isupper():
                    fileID.append(result[0])
                else:
                    fileID.append(result[0][:-1])
            else:
                if result[0][-1].islower() or result[0][-2].islower():
                    fileID.append(result[0][:-2])
                else:
                    fileID.append(result[0][:-1])
    else:
        file_list.remove(filename)
    
df = pd.DataFrame({'filename': file_list, 'Document ID': fileID})

os.chdir(current_path)
df.to_csv(args.file, index = False)