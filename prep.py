import re

def preprocess(file):
    with open(file, "r") as f:
        f.seek(0)
        content = f.read()
        content = content.lower()
        out = re.sub(r"\d","", content)
        out = re.sub(r"\W", " ", out)
        out = re.sub(r"\s+", " ", out)
        return out