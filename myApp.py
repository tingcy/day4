import streamlit as st

st.write('Hello SHRDC')
st.write("hello again from SHRDC")
st.write("hello the third time!")
st.error("error")

select1 = st.selectbox("Kuala Lumpur is located at",
['Malaysia', 'Thailand', 'UK'])

st.write("you have selected: ", select1)

st.multiselect("Select 2 states",
['Selangor','Johor','Kedah'])

c1 = st.button("click me")
if c1:
    st.write("you have clicked the button")

number = st.number_input("Insert a number",
                         value=None, placeholder="Type a number...")

from PIL import Image
im = Image.open('shrdc.jpeg')
st.image(im, width=300)

import pandas as pd
df = pd.read_excel('sampleData.xlsx')
st.dataframe(df)



tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

col1, col2, col3 = st.columns(3)
with col1:
    st.bar_chart(df, x='Location', y='Income')    
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.slider("Select the length of stay", 1,10, value=3)
