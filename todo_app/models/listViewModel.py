import todo_app.models.todoItem as todoItem

class ListViewModel():
    def __init__(self, items: list):
        self.id = id
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def not_started_items(self):
        return [item for item in self._items if item.status == todoItem.TodoItemStatus.NOT_STARTED]
    
    @property
    def in_progress_items(self):
        return [item for item in self._items if item.status == todoItem.TodoItemStatus.IN_PROGRESS]
    
    @property
    def complete_items(self):
        return [item for item in self._items if item.status == todoItem.TodoItemStatus.COMPLETE]

    def __str__(self):
        list_string = ""
        for item in self._items:
            list_string = f"{list_string}\n{item}"
        return list_string
    