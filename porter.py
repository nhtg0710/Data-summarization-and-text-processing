import nltk
from prep import preprocess

ps = nltk.PorterStemmer()

def porter(file):
    stemmed = []
    content = preprocess(file).split()
    for word in content:
        stemmed.append(ps.stem(word))
    return stemmed