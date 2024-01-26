import streamlit as st
import functions as fu

st.title("My Todo App")
st.subheader("This is something new")
todos = fu.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    fu.write_todos(todos)

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fu.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add something", placeholder="Add a new todo..",
                      on_change=add_todo, key='new_todo')

