import functions
import streamlit as st

st.title("My Todo App")
st.subheader('This is my todo app')
st.write("Aim to increase your productivity")

todos = functions.read_todos()
for item in todos:
    st.checkbox(item)

st.text_input(label= 'Enter a new-todo',
                              label_visibility= "hidden",
                              placeholder='Add new todo...')


