import pytest
import todo_app.models.listViewModel as listViewModel
import todo_app.models.todoItem as todoItem

@pytest.fixture
def mock_not_started_items():
   return [
      todoItem.TodoItem("test_not_started_0", "not_started_0", todoItem.TodoItemStatus.NOT_STARTED),
   ]

@pytest.fixture
def mock_in_progress_items():
   return [
      todoItem.TodoItem("test_in_progress_0", "in_progress_0", todoItem.TodoItemStatus.IN_PROGRESS),
   ]

@pytest.fixture
def mock_completed_items():
   return [
      todoItem.TodoItem("test_completed_0", "completed_0", todoItem.TodoItemStatus.COMPLETE),
   ]

@pytest.fixture
def mock_list_items(mock_not_started_items, mock_in_progress_items, mock_completed_items):
    return mock_not_started_items + mock_in_progress_items + mock_completed_items

def test_get_items(mock_list_items):
   # arrange
   view_model = listViewModel.ListViewModel(mock_list_items)

   # act
   items = view_model.items

   # assert
   assert(len(items) == len(mock_list_items))
   for id in mock_list_items:
      assert(id in items)   

def test_get_not_started_items(mock_list_items, mock_not_started_items):
    # arrange
    view_model = listViewModel.ListViewModel(mock_list_items)

    # act
    not_started_items = view_model.not_started_items

    # assert
    assert(len(not_started_items) == len(mock_not_started_items))
    for item in mock_not_started_items:
       assert(item in not_started_items)

def test_get_in_progress_items(mock_list_items, mock_in_progress_items):
    # arrange
    view_model = listViewModel.ListViewModel(mock_list_items)

    # act
    in_progress_items = view_model.in_progress_items

    # assert
    assert(len(in_progress_items) == len(mock_in_progress_items))
    for item in mock_in_progress_items:
       assert(item in in_progress_items)

def test_get_completed_items(mock_list_items, mock_completed_items):
    # arrange
    view_model = listViewModel.ListViewModel(mock_list_items)

    # act
    completed_items = view_model.complete_items

    # assert
    assert(len(completed_items) == len(mock_completed_items))
    for item in mock_completed_items:
       assert(item in completed_items)