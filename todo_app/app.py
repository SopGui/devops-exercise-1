from flask import Flask, render_template
import os;

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

def read_todos(filename):
    print(os.getcwd())
    with open(filename, 'r') as todo_file:
        todo_items = todo_file.read()
    return todo_items.split('\n')

@app.route('/')
def index():
   todos = read_todos('todo_app/todos.txt')
   return render_template('index.html', todos=todos)
