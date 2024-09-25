# -*- coding: utf-8 -*-
"""NLP Project - Semantic Analysis of Restaurant Reviews.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YlS-Lshb-9IrPJT1HCrBgxzQHn1eMzjK
"""

import warnings
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Dataset Link: https://drive.google.com/file/d/1XKsBaDjjIftNdbm_02beVBlK8AuCemfX/view?usp=sharing"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/BI/ML Master Files/ML Master Files/Restaurant_Reviews (1).tsv', delimiter='\t', quoting=3)

df.shape

df['Review']

# input(review)   --->   model  ---->  output(Sentiment of the review)
# sentiment = model(review)

df['Review'][0]

df['Review'][1]

df['Review'][3]

# sentiment(+ve or -ve) <-  model("review")

df.Liked.value_counts()

df.shape

df.info()

df['Liked'].value_counts()

df.isna().sum()

df['Review'][999]

df.tail()

# That restaurant is very good....... ,,,, :) I liked the services @ that restaurant. #happy I liked the food.....

"""#**Data Cleaning**

##Removing punctuations
"""

import string
string.punctuation

print(df['Review'][0])

text = df['Review'][0]
print(text)

print(text)
# Regex - Regular expressions
import re
review = re.sub( '[^a-zA-Z]' , ' ' , text )
print(review)

re.sub( '[^a-zA-Z]' , ' ' , "We are learning @nlp , ,,, ,### 1234 don't we do it." )

review = review.lower()
print(review)

import re
def rem_punc(text):
  review = re.sub( '[^a-zA-Z]' , ' ' , text )
  return review

df['Review'] = df['Review'].apply(rem_punc)

df.head(10)

"""#**Removing stopwords**"""

#natural language toolkit
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

len(stopwords.words('english'))

# i like this place very much.

len(stopwords.words('english'))

stopwords.words('german')

stopwords.words('french')

review

stopwords_list  = stopwords.words('english')

review = 'Wow  Is are the The Loved this place'
review = review.split()
print(review)

clean_review = []
for word in review:
  word = word.lower()
  if(word not in stopwords_list):
    clean_review.append(word)

clean_review

' '.join(clean_review)

# Tokenization => list of words
review = 'Wow  Is are the The Loved this place'
review = review.split()
print(review)

stopwords_list = stopwords.words('english')

normal_word = []
for word in review:
  if(word.lower() not in stopwords_list):
    normal_word.append(word)
print('\n')
print('normal_word:', normal_word)

' '.join(normal_word)

review

review = 'Wow  Is are the The Loved this place'
print(review)

def rem_stopwords(text):
  text = text.split()
  clean_review=[]
  for word in text:
    if(word.lower() not in stopwords.words('english')):
      clean_review.append(word)

  return ' '.join(clean_review)

rem_stopwords(review)

# Removing stopwords
df['Review'] = df['Review'].apply(rem_stopwords)

df.tail(10)

"""#**Stemming & Lemmatization**"""

# Stemming -> respon
# Lemmatization -> response

# response , responses, respond , responding  => response
# like , liked , likes  => like

#-- root words

#1.respon
#2.response

from nltk.stem.snowball import SnowballStemmer

# create an object of stemming function
stemmer = SnowballStemmer("english")

def stemming(text):
    '''a function which stems each word in the given text'''

    text = [stemmer.stem(word) for word in text.split()]

    return " ".join(text)

df['Review'] = df['Review'].apply(stemming)

df.head()

df.shape

from sklearn.feature_extraction.text import CountVectorizer

# Example corpus (list of documents)
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

#step 1 : this, is , the ,first, document, second, And, third, one  # vocab/ features
  #  r1       1  1  1 1 1 0 0 0 0
  #  r2       1  1  1 0 2 1 0 0 0
  #  r3
  #  r4

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer to the corpus and transform the documents into a document-term matrix
X = vectorizer.fit_transform(corpus)

# Get the vocabulary (list of unique words)
vocab = vectorizer.get_feature_names_out()
# Display the vocabulary
print("\nVocabulary:")
print(vocab)

# Convert the document-term matrix to a dense array and display it
print("Document-Term Matrix:")
print(X.toarray())

# 'This is the first document.

# Bag of Words: CountVectorizer()

corpus1 = []
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

# print(review)
corpus1.append(review)
# print(corpus1)
X = cv.fit_transform(corpus1)

cv.get_feature_names_out()

X

X.toarray()

df.shape

df.head()

df.tail()

import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]',' ', df['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ ps.stem(word) for word in review if not word in set(stopwords.words('english')) ]
    review = ' '.join(review)
    print(review)
    corpus.append(review)

corpus

corpus_dataset = pd.DataFrame(corpus)
corpus_dataset.head()

corpus_dataset.columns=['corpus']

corpus_dataset.head()

corpus_dataset.to_csv('corpus_dataset.csv')

type(corpus_dataset)

type(corpus)
corpus

df['Review']

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

X = cv.fit_transform(df['Review']).toarray()

X

X.shape

X[0]

len(X[0])

X.shape

len(X)
df

X

y = df['Liked'].values

# df.iloc[:,1].values

y = df.iloc[:,1].values

y.shape

cv.get_feature_names_out()

len(cv.get_feature_names_out())

df.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# naive bayes model

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# classifier.predict(X_test)

y_pred = classifier.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix

accuracy_score(y_test, y_pred)

confusion_matrix(y_test, y_pred)

"""### Test our model on real time data"""

Review = "It's a nice service."
Review = rem_punc(Review)
Review = rem_stopwords(Review)
Review

Review = "bad service"
# removing punctuation
Review = rem_punc(Review)
# removing stopwords
Review = rem_stopwords(Review)

input_data = [Review]

# applying cv.transform
input_data = cv.transform(input_data).toarray()
# prediction
input_pred = classifier.predict(input_data)

if input_pred[0]==1:
    print("Review is Positive")
else:
    print("Review is Negative")

# converting to a function

def sentiment_predictor(Review):
    # removing punctuation
    Review = rem_punc(Review)
    # removing stopwords
    Review = rem_stopwords(Review)

    input_data = [Review]

    # applying cv.transform
    input_data = cv.transform(input_data).toarray()
    # prediction
    input_pred = classifier.predict(input_data)

    if input_pred[0]==1:
        res = "Review is Positive"
    else:
        res = "Review is Negative"
    return res

sentiment_predictor(input('Give your review here: '))

sentiment_predictor(input('Give your review here: '))

Review = "Wow wonderful"

input_data = [Review]
input_data = cv.transform(input_data).toarray()
input_pred = classifier.predict(input_data)

if input_pred[0]==1:
    print("Review is Positive")
else:
    print("Review is Negative")

"""# Happy Learning"""