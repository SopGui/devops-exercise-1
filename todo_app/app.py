from flask import Flask, request, render_template, redirect
from todo_app.todoItems.todoItemManager import todo_list

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
   todos = todo_list.get_todos()
   return render_template('index.html', todos=todos)

@app.route('/add-item', methods=['POST'])
def add_item():
    new_item = request.form.get('new-item')
    todo_list.add_todo(new_item)
    return redirect('/', code=302)
    
@app.route('/delete-item/<item_id>', methods=['POST'])
def delete_item(item_id):
    todo_list.delete_todo(item_id)
    return redirect('/', code=302)

@app.route('/toggle-check-item/<item_id>', methods=['POST'])
def toggle_check_item(item_id):
    print(item_id)
    return redirect('/', code=302)