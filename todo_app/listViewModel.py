import todo_app.api.todoItem as todoItem

class ListViewModel():
    def __init__(self, items: list):
        self.id = id
        self._items = items

    @property
    def items(self):
        return self._items

    def __str__(self):
        list_string = ""
        for item in self._items:
            list_string = f"{list_string}\nCard - ID: {item.id} Title: {item.title}, Status: {item.status}"
        return list_string
        