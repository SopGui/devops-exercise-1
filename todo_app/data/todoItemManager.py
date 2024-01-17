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
        new_todo = {'id': str(uuid.uuid4()), 'title': new_item_title,'status': "Not started" }
        self.todo_list.append(new_todo)
        self.save_todos_to_file()

    def delete_todo(self, id_to_delete):
        todo_list_without_id_to_delete = [todo_item for todo_item in self.todo_list if todo_item["id"] != id_to_delete]

        if not len(todo_list_without_id_to_delete) < len(self.todo_list):
            return False

        self.todo_list = todo_list_without_id_to_delete
        self.save_todos_to_file()

        return True
    
    def set_item_status(self, id_to_set, new_status):
        for todod_item_index in range(len(self.todo_list)):
            todo_item = self.todo_list[todod_item_index]

            if not todo_item["id"] == id_to_set:
                continue

            todo_item["status"] = new_status
            self.save_todos_to_file()
            return True
            
        return False
    
todo_list = TodoList("todo_app/data/todos.json")
    

    
         
