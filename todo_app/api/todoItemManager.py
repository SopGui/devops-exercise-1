import json
import uuid
import todo_app.api.trelloApi as trelloApi

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.todo_list = self.load_todos()

    def load_todos(self):
        return trelloApi.get_cards()

    def get_todos(self):
        return self.todo_list
    
    def add_todo(self, new_item_title):
        new_todo = trelloApi.create_card(new_item_title)
        self.todo_list.append(new_todo)

    def delete_todo(self, id_to_delete):
        todo_list_without_id_to_delete = [todo_item for todo_item in self.todo_list if todo_item["id"] != id_to_delete]

        if not len(todo_list_without_id_to_delete) < len(self.todo_list):
            return False
        
        self.todo_list = todo_list_without_id_to_delete

        trelloApi.delete_card(id_to_delete)
        return True
    
    def set_item_status(self, id_to_set, new_status):
        # for todo_item in self.todo_list:
        #     if not todo_item["id"] == id_to_set:
        #         continue

        #     todo_item["status"] = new_status
        #     self.save_todos_to_file()
        #     return True

        # TODO: Reimplement
            
        return False
    
todo_list = TodoList("todo_app/data/todos.json")