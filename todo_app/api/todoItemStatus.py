from enum import Enum

class Todo_item_status(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    COMPLETE = 3

enum_string_value_lookup = {
    "Not Started" : Todo_item_status.NOT_STARTED,
    "In Progress" : Todo_item_status.IN_PROGRESS,
    "Complete" : Todo_item_status.COMPLETE
}

# TODO When create class, can use this when getting status from class
string_enum_value_lookup = {
    Todo_item_status.NOT_STARTED : "Not started",
    Todo_item_status.IN_PROGRESS : "In Progress",
    Todo_item_status.COMPLETE : "Complete"
}