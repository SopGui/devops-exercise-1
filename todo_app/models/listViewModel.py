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
        return list(filter(lambda item: item.status == todoItem.TodoItemStatus.NOT_STARTED, self._items))
    
    @property
    def in_progress_items(self):
        return list(filter(lambda item: item.status == todoItem.TodoItemStatus.IN_PROGRESS, self._items))
    
    @property
    def complete_items(self):
        return list(filter(lambda item: item.status == todoItem.TodoItemStatus.COMPLETE, self._items))

    def __str__(self):
        list_string = ""
        for item in self._items:
            list_string = f"{list_string}\nCard - ID: {item.id} Title: {item.title}, Status: {item.status}"
        return list_string
        