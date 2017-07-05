import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#NB naive bayes

def readFiles(path):
    i=0
    for root, dirnames, filenames in os.walk(path):
#        print(root,dirnames,filenames)
        for filename in filenames:
            path = os.path.join(root, filename)
            inBody = False
            
            if i<10:
                print(i,path)
            i+=1
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message
            
def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

#data = DataFrame({'message': [], 'class': []})

#data = data.append(dataFrameFromDirectory('/Users/angelaburden/Documents/DataScience/emails/spam', 'spam'))
#data = data.append(dataFrameFromDirectory('/Users/angelaburden/Documents/DataScience/emails/ham', 'ham'))
#vectorizer = CountVectorizer()
#counts = vectorizer.fit_transform(data['message'].values)
#this is a 4500 * long matrix of word vs occurrence for each email SPARSE MATRIX
#^^^^^converts all words seen into numbers (tokenises) and count how many times each word occurs
#classifier = MultinomialNB()
#targets = data['class'].values
#there are 4500 emails, this gives a list of 4500 classifications
#classifier.fit(counts, targets)

#examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]
#example_counts = vectorizer.transform(examples)
#predictions = classifier.predict(example_counts)
#predictions