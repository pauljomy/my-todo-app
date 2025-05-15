import streamlit as sl
import todo_fun as tf

todos = tf.get_todos()

def add_todo():
    todo = sl.session_state["user_input"].strip() + "\n"
    todos.append(todo)
    tf.write_todos(todos)
    sl.session_state["user_input"] = ""

sl.title("My Todo App")
sl.subheader("This is my todo app")

for index,todo in enumerate(todos):
    check_box = sl.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        tf.write_todos(todos)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input(label = "",placeholder="Add new todo",
              on_change=add_todo, key="user_input")
