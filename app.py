import streamlit as st
import pandas as pd
st.title("My First Web app")
st.set_page_config(page_icon="😒",page_title="MY FIRST APP",layout='wide')
st.header("Header")
st.subheader("subheader")
st.text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
#display
a=1000
s="hello Sristy"
st.write(s)
st.write(a)
df=pd.read_csv("netflix_titles.csv")
st.dataframe(df)
st.subheader("input widgets")
name=st.text_input("Name: ",placeholder="type your name")
pwd=st.text_input("Password: ",placeholder="type your password",type="password")
st.write(name)
st.write(pwd)
content=st.text_area("comment: ",placeholder="type something")
age=st.number_input("age: ",min_value=1,max_value=100)
st.write(age)
st.slider("select: ",min_value=1,max_value=1000,step=100,value=250)
country=st.selectbox("country: ",options=["india","korea","france","usa"],disabled=True)

st.write(country)
if st.button("click me👌"):
    st.text("ghjgshbhj")
if st.button("Display immages"):
    st.image("image/batman.jpg")
    st.columns(2,border=True)
    gender= st.radio("gender: ",options=["m","f"])
    st.image("image/cat.jpg")
    st.tabs("home")  
    tab1 = st.tabs(["Home", "About"])   