import pandas as pd
import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

data=pd.read_csv("dataset.csv",encoding="utf-8")
st.header("Dataset : ")
st.write(data.head())

def processing(text):
    # Tokenize
    st.header("Tokens")
    tokens = nltk.word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum()]
    st.write(tokens)

    # Remove Stopwords
    st.header("Stop Words")
    stop_words = set(stopwords.words('english'))
    st.write(stop_words)
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatization
    st.header("Lemmatizer")
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    st.write("Lemmatized Tokens : ")
    st.write(tokens)

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    return tokens

# Process the review text column]
data['text_process'] = data['Review Text'].apply(processing)

# Print some values
st.header("Processed Data")
st.write(data['text_process'].head(10))

