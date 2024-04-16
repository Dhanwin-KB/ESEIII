import streamlit as st
import pandas as pd
import plotly.express as px

cart_trends = pd.read_csv("dataset.csv")

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.sidebar.header('Select')

select_features_3d = st.sidebar.multiselect('Select features for 3D Graph', ['Age', 'Rating', 'Positive Feedback Count'])
selected_features_scatter = st.sidebar.selectbox('Select feature for Scatterplot', ['Age', 'Positive Feedback Count', 'Rating'])

average_age = cart_trends['Age'].mean()
average_rating = cart_trends['Rating'].mean()
total=cart_trends['Age'].count()

st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Average Age of Customers", average_age)
col2.metric("Average Rating of Products", average_rating)
col3.metric("Total Orders", total)

st.markdown('### 3D Graph')
fig_3d = None
if len(select_features_3d) >= 3:
    fig_3d = px.scatter_3d(cart_trends, x=select_features_3d[0], y=select_features_3d[1], z=select_features_3d[2], color='Recommended IND')
    st.plotly_chart(fig_3d)
else:
    st.warning("Please select at least three features for the 3D graph.")

st.markdown('### Scatter Plot - Class vs Selected Feature (Scatterplot)')
fig_scatter = px.scatter(cart_trends, x='Class Name', y=selected_features_scatter, color='Age')
st.plotly_chart(fig_scatter)


