# Part B Task 2
import re
import os
import sys
from prep import preprocess

folder = sys.argv[1][:-7]
file = sys.argv[1][-7:]
path = os.path.abspath(folder)
current_dir = os.getcwd()
os.chdir(path)

sys.stdout.write(preprocess(file))
os.chdir(current_dir) 