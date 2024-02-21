from flask import Flask, request, render_template, redirect, abort
from todo_app.api.todoItemManager import todo_list

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
    if todo_list.delete_todo(item_id):
        return redirect('/', code=302)
    abort(404)

@app.route('/set_item_status/<new_status>/<item_id>', methods=['POST'])
def set_item_status(new_status, item_id):
    if todo_list.set_item_status(item_id, new_status):
        return redirect('/', code=302)
    abort(404)