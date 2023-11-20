import streamlit as st
from PIL import Image

st.title("Calculator")
img = Image.open("viv.jpg")
st.sidebar.image(img)

col1, col2, col3 = st.columns(3)

def add(a,b) : # name
    c = a + b # argument and action
    return c  #result


def sub(a,b) :
    c = a - b
    return c


def mul(a,b) :
    c = a * b
    return c


x = st.number_input("Input first number")
y = st.number_input("Input second number")

with col1:
    if st.button("Add"):
     st.write(add(x,y))

with col2:
    if st.button("Subtract"):
        st.write(sub(x,y))

with col3:
    if st.button("Multiply"):
        st.write(mul(x,y))