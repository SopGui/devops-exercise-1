import pytest
import todo_app.models.listViewModel as listViewModel
import todo_app.models.todoItem as todoItem

class MockedCard():
   def __init__(self, id: str, title: str, status: todoItem.TodoItemStatus):
      self.id = id
      self.title = title
      self.status = status

@pytest.fixture
def mock_not_started_items():
   return [
      MockedCard("test_not_started_0", "not_started_0", todoItem.TodoItemStatus.NOT_STARTED),
   ]

@pytest.fixture
def mock_in_progress_items():
   return [
      MockedCard("test_in_progress_0", "in_progress_0", todoItem.TodoItemStatus.IN_PROGRESS),
   ]

@pytest.fixture
def mock_completed_items():
   return [
      MockedCard("test_completed_0", "completed_0", todoItem.TodoItemStatus.COMPLETE),
   ]

@pytest.fixture
def mock_list_items(mock_not_started_items, mock_in_progress_items, mock_completed_items):
    return mock_not_started_items + mock_in_progress_items + mock_completed_items

def test_divisible_by_3():
   assert 9 % 3 == 0

def test_get_items(mock_list_items):
   # arrange

   # act
   view_model = listViewModel.ListViewModel(mock_list_items)

   # assert
   assert(len(view_model.items) == len(mock_list_items))
   for id in mock_list_items:
      assert(id in view_model.items)   

def test_get_not_started_items(mock_list_items, mock_not_started_items):
    # arrange

    # act
    view_model = listViewModel.ListViewModel(mock_list_items)

    # assert
    assert(len(view_model.not_started_items) == len(mock_not_started_items))
    for id in mock_not_started_items:
       assert(id in view_model.not_started_items)

def test_get_in_progress_items(mock_list_items, mock_in_progress_items):
    # arrange

    # act
    view_model = listViewModel.ListViewModel(mock_list_items)

    # assert
    assert(len(view_model.in_progress_items) == len(mock_in_progress_items))
    for id in mock_in_progress_items:
       assert(id in view_model.in_progress_items)


def test_not_started_items(mock_list_items, mock_completed_items):
    # arrange

    # act
    view_model = listViewModel.ListViewModel(mock_list_items)

    # assert
    assert(len(view_model.complete_items) == len(mock_completed_items))
    for id in mock_completed_items:
       assert(id in view_model.complete_items)