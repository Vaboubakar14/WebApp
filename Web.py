import streamlit as st
import func

todos = func.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + "\n")
    func.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo app.")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="Enter a todo:", placeholder="Add new todo:",
              label_visibility="collapsed", key="new_todo",
              on_change=add_todo)
