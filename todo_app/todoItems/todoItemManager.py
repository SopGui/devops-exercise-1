FILENAME = "todo_app/todoItems/todos.json"
import json
import uuid

def get_todos():
    with open(FILENAME, 'r') as todo_file:
        todo_items = todo_file.read()
    return json.loads(todo_items)

def add_todo(new_item):
    entry = {'id': str(uuid.uuid4()), 'title': new_item}
    todos = get_todos()
    todos.append(entry)

    with open(FILENAME, 'w') as todo_file:
        json.dump(todos, todo_file)
