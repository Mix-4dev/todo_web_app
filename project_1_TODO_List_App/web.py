import functions
import streamlit as st

todos: list[str] = functions.read_todos()
def add_todo() -> None:
    """When user press enter the add_todo is called and
    the whole script is executed"""
    todo:str = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader('This is my todo app')
st.write("Aim to increase your productivity")

for index,item in enumerate(todos):
    check_box = st.checkbox(item, key= item)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label='Enter a new-todo',
              label_visibility="hidden",
              placeholder='Add new todo...',on_change=add_todo,key='new_todo')