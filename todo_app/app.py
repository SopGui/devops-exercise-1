from flask import Flask, request, render_template, redirect
from todo_app.todoItems.todoItemManager import get_todos, add_todo

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
   todos = get_todos()
   return render_template('index.html', todos=todos)

@app.route('/add-item', methods=['POST'])
def add_item():
    new_item = request.form.get('new-item')
    add_todo(new_item)
    return redirect('/', code=302)
    
    