import json
import uuid

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.todo_list = self.read_todos_from_file()

    def read_todos_from_file(self):
        with open(self.filename, 'r') as todo_file:
            todos_from_file = todo_file.read()
        return json.loads(todos_from_file)
    
    def save_todos_to_file(self):
        with open(self.filename, 'w') as todo_file:
            json.dump(self.todo_list, todo_file)

    def get_todos(self):
        return self.todo_list
    
    def add_todo(self, new_item_title):
        new_todo = {'id': str(uuid.uuid4()), 'title': new_item_title }
        self.todo_list.append(new_todo)
        self.save_todos_to_file()

    def delete_todo(self, id_to_delete):
        todo_list_without_id_to_delete = [todo_item for todo_item in self.todo_list if todo_item["id"] != id_to_delete]

        if not len(todo_list_without_id_to_delete) < len(self.todo_list):
            return False

        self.todo_list = todo_list_without_id_to_delete
        self.save_todos_to_file()

todo_list = TodoList("todo_app/todoItems/todos.json")
    

    
         
