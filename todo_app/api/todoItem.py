from enum import Enum

class TodoItemStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETE = 3

not_started_text = "Not Started"
in_progress_text = "In Progress"
complete_text = "Complete"

def get_string_as_todo_item_status(status_string: str):
    if status_string == not_started_text:
        return TodoItemStatus.NOT_STARTED
    if status_string == in_progress_text:
        return TodoItemStatus.IN_PROGRESS
    if status_string == complete_text:
        return TodoItemStatus.COMPLETE
    return None

def get_todo_item_status_as_string(status: TodoItemStatus):
    if status == TodoItemStatus.NOT_STARTED:
        return not_started_text
    if status == TodoItemStatus.IN_PROGRESS:
        return in_progress_text
    if status == TodoItemStatus.COMPLETE:
        return complete_text
    return "unkown"

def get_colour_from_status(status: TodoItemStatus):
    if status == TodoItemStatus.NOT_STARTED:
        return "dark"
    if status == TodoItemStatus.IN_PROGRESS:
        return "primary"
    if status == TodoItemStatus.COMPLETE:
        return "success"
    return "unknown"

class TodoItem():
    def __init__(self, id: str, title: str, status):
        self.id = id
        self.title = title

        if type(status) == TodoItemStatus:
            self.status = status
        else:
            self.status = get_string_as_todo_item_status(status)

    def get_status_as_string(self):
        return get_todo_item_status_as_string(self.status)
    
    def get_colour_class(self):
        return f"bg-{get_colour_from_status(self.status)}"
    
    def __str__(self):
       return f"Card - ID: {self.id} Title: {self.title}, Status: {self.status}"
        
