import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.get_write_file(todos)



todos = functions.get_read_file()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
