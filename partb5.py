## Part B Task 5
import re
import os
import sys
import numpy as np
import pandas as pd
import nltk

from porter import porter
from prep import preprocess
from sklearn.feature_extraction.text import TfidfTransformer

ps = nltk.PorterStemmer()

def cos_similarity(vec1,vec2):
    return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))

current_path = os.getcwd()
keyword_list = sys.argv[1:]
path = os.path.abspath("cricket")
os.chdir(path)
keyword_file = []

file_list = sorted(list(filter(os.path.isfile, os.listdir(path))))

# the collection of filenames of files with keywords
for filename in file_list:
    content = ' '.join(porter(filename))
    has_keyword = True
    for word in keyword_list:
        if ps.stem(word) not in content:
            has_keyword = False
    if has_keyword:
        keyword_file.append(filename)
os.chdir(current_path)
doc_ID = pd.read_csv('partb1.csv')
doc_ID = doc_ID.set_index('filename')
os.chdir(path)

# document IDs of files with keyword
doc_ID_list = list(doc_ID.loc[doc_ID.index.isin(keyword_file)]['Document ID'].values)

if doc_ID_list:
    os.chdir(current_path)
    doc_ID = pd.read_csv('partb1.csv')
    doc_ID = doc_ID.set_index('Document ID')
    os.chdir(path)
    all_vocab = []
else:
    print("Found no documents")
    sys.exit()
for ID in doc_ID_list:
    filename = doc_ID.loc[ID, 'filename']
    words = porter(filename)
    all_vocab += words

vocab_set = list(set(all_vocab))

sim_score = {} # score dictionary for corresponding files
term_count = []

for ID in doc_ID_list:
    filename = doc_ID.loc[ID, 'filename']
    words = porter(filename)
    temp_vec = []
    for word in vocab_set:
        temp_vec.append(words.count(word))
    term_count.append(temp_vec)

# tfidf
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(term_count)
doc_tfidf = tfidf.toarray()

stem_keyword = [ps.stem(word) for word in keyword_list]
query = []
query_unit = []

for word in vocab_set:
    query.append(stem_keyword.count(word))
for vec in query:
    query_unit.append(vec/np.linalg.norm(query))

# cosine similarity
sim = [cos_similarity(query_unit, doc_tfidf[d_id]) for d_id in range(doc_tfidf.shape[0])]

for i in range(len(sim)):
        sim_score[doc_ID_list[i]] = sim[i]
        
# sorting files for ranking
sim_score = {key: value for key, value in sorted(sim_score.items(), key=lambda item: item[1], reverse=True)}
final_score = pd.DataFrame(sim_score.items(), columns=["Document ID", "score"])
print(final_score)
os.chdir(current_path)