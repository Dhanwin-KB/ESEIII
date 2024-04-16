import pandas as pd
import streamlit as st
import nltk
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

data=pd.read_csv("dataset.csv",encoding="utf-8")
st.header("Dataset : ")
st.write(data.head())

def processing(text):
    # Tokenize
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()]

    # Remove Stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return tokens

# Process the review text column]
data['text_process'] = data['text'].apply(processing)

#print some values
print(data['text_process'].head(10))

# Jaccard Similarity
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union

    # Open the text file for reading
with open('Text1.txt', 'r', encoding='utf-8') as file:
    Text1= file.read()

with open('Text2.txt', 'r', encoding='utf-8') as file:
    Text2= file.read()

tokens1 = set(processing(Text1))
tokens2 = set(processing(Text2))

similarity_score = jaccard_similarity(tokens1, tokens2)
print(f"Jaccard Similarity: {similarity_score}")
print(f"Tokens 1: {tokens1}\nTokens 2: {tokens2}")

vectorizer = TfidfVectorizer()
vector1 = vectorizer.fit_transform([' '.join(tokens1)])
vector2 = vectorizer.transform([' '.join(tokens2)])

#Cosine Similarity
cos_similarity = cosine_similarity(vector1, vector2)
print(f"Cosine Similarity:\n{cos_similarity}")

# Plotting the similarity scores
scores = [0.22837370242214533, 0.5935921]
methods = ['Jaccard Similarity', 'Cosine Similarity']

# Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(methods, scores, color=['blue', 'green'])
plt.xlabel('Similarity Method')
plt.ylabel('Similarity Score')
plt.title('Comparison of Similarity Scores')
plt.ylim(0, 1)  # Set the y-axis limit from 0 to 1
plt.show()
