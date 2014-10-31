# word counter from text file#

# imports

from sys import argv
from collections import Counter

#global variables
words = []

#opening file and assigning all values in file to iterate

for lines in open(argv[1],'r').readlines():
      for word in lines.strip().split():
            words.append(word.lower())

#counting words

w_count = Counter(words)


#display result

for word,count in sorted(w_count.items()):
      print(word + '=>',count)

            

            
            
