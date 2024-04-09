from flask import Flask, request, render_template, redirect, abort
import todo_app.api.trelloApi as trelloApi
import todo_app.models.todoItem as todoItem
import todo_app.models.listViewModel as listViewModel

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
   todos = trelloApi.get_cards()
   view_model = listViewModel.ListViewModel(todos)
   return render_template('index.html', todos=view_model)

@app.route('/add-item', methods=['POST'])
def add_item():
    new_item = request.form.get('new-item')
    trelloApi.create_card(new_item, todoItem.TodoItemStatus.NOT_STARTED)
    return redirect('/', code=302)
    
@app.route('/delete-item/<item_id>', methods=['POST'])
def delete_item(item_id):
    trelloApi.delete_card(item_id)
    return redirect('/', code=302)

@app.route('/set_item_status/<new_status>/<item_id>', methods=['POST'])
def set_item_status(new_status, item_id):
    trelloApi.set_card_status(item_id, todoItem.get_string_as_todo_item_status(new_status))
    return redirect('/', code=302)