import streamlit as st
import functions

todos = functions.get_read_file()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")
