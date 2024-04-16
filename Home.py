import streamlit as st
import pandas as pd
import plotly.express as px

shopping_trends = pd.read_csv("dataset.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.header("E-Commerce Website Platform Exclusive For Women")

st.text("This website will showcase the analysis and insights from the dataset containing the entries of Women E-Commerce Website.")

st.text("Dress 1")
st.image("image1.jpg")
st.text("Dress 2")
st.image("image2.jpg")
st.text("Dress 3")
st.image("image3.jpg")
st.text("Dress 4")
st.image("image4.jpg")


