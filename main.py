import streamlit as st
import pandas
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Jaquan Rhodes")
    content = """
    Hi, I am an Software Development Student at ECPI University. 
    I graduate in May 2024 with my Bachelors in Computer Information & Science. 
    """
    st.info(content)

content2 = """
Below you can find some of my projects i have built in Python. Feel free to contact me.
"""
st.write(content2)

col3, emptyCol, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("pythonProject/data.csv", sep=";")
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[{row['title']}]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[{row['title']}]({row['url']})")


