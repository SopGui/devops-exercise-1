import pytest
import listViewModel
import todoItem

def create_mocked_card(id: str, title: str, status: todoItem.TodoItemStatus):
   return {
      id: id,
      title: title,
      status: status
   }

@pytest.fixture
def mock_list_items():
    return [
       create_mocked_card("test", "title", todoItem.TodoItemStatus.NOT_STARTED),
       create_mocked_card("test", "title", todoItem.TodoItemStatus.IN_PROGRESS),
       create_mocked_card("test2", "title2", todoItem.TodoItemStatus.COMPLETE)
    ]

def test_divisible_by_3():
   assert 9 % 3 == 0

def test_get_items(mock_list_items):
   view_model = listViewModel.ListViewModel(mock_list_items)

   assert(len(view_model.items) == len(mock_list_items))
       