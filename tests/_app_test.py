from dotenv import load_dotenv, find_dotenv
from todo_app import app
from todo_app.api import trelloApi

import pytest
import os
import requests

def get_board_id():
    return os.getenv('TRELLO_BOARD_ID')

def get_not_started_list_id():
    return os.getenv('NOT_STARTED_LIST_ID')

def get_in_progress_list_id():
    return os.getenv('IN_PROGRESS_LIST_ID')
    
def get_complete_list_id():
    return os.getenv('COMPLETE_LIST_ID')

def get_api_key():
    return os.getenv('TRELLO_API_KEY')

def get_api_token():
    return os.getenv('TRELLO_API_TOKEN')

testing_consts = {
    'test_card_id': '456',
    'test_card_name': 'Test card',
}

def form_get_stub(key):
    if key == "new-item":
        return testing_consts["test_card_name"]

def request_stub(method, url, data={}):
    if method == "GET" and url == f'https://api.trello.com/1/boards/{get_board_id()}/cards?key={get_api_key()}&token={get_api_token()}':
        fake_response_data = [{'id': testing_consts['test_card_id'], 'name': testing_consts['test_card_name'], 'idList': get_not_started_list_id()}]
        return StubResponse(fake_response_data, 200)
    
    if method == "POST" and url == f"https://api.trello.com/1/cards?idList={get_not_started_list_id()}&key={get_api_key()}&token={get_api_token()}":
        if "name" in data and data["name"] == testing_consts["test_card_name"]:
            return StubResponse([], 200)
        
    if method == "DELETE" and url == f"https://api.trello.com/1/cards/{testing_consts['test_card_id']}?key={get_api_key()}&token={get_api_token()}":
        return StubResponse([], 200)
    
    if method == "PUT" and url == f"https://api.trello.com/1/cards/{testing_consts['test_card_id']}?key={get_api_key()}&token={get_api_token()}":
        if "idList" in data and data["idList"] in [get_not_started_list_id(), get_in_progress_list_id(), get_complete_list_id()]:
            return StubResponse([], 200)

    raise Exception(f'Integration test did not expect URL "{url}" with method "{method}" and data "{data}"')

class StubResponse():
    def __init__(self, fake_response_data, status_code, text=None):
        self.fake_response_data = fake_response_data
        self._status_code = status_code
        self._text = text

    @property
    def status_code(self):
        return self._status_code
    
    @property
    def text(self):
        return self._text

    def json(self):
        return self.fake_response_data
    
@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'request', request_stub)

    response = client.get('/')
    assert(response.status_code == 200)
    assert(testing_consts['test_card_id'] in response.data.decode())
    assert(testing_consts['test_card_name'] in response.data.decode())

def test_create_item_endpoint(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'request', request_stub)

    monkeypatch.setattr(app, 'get_from_request', form_get_stub)

    create_response = client.post('/add-item')
    assert(create_response.status_code == 302)

def test_create_item_endpoint(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'request', request_stub)

    create_response = client.post(f'/delete-item/{testing_consts["test_card_id"]}')
    print(f'/delete_item/{testing_consts["test_card_id"]}')
    assert(create_response.status_code == 302)

def test_update_status_item_endpoint(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'request', request_stub)

    create_response = client.post(f'/set-item-status/Not Started/{testing_consts["test_card_id"]}')
    assert(create_response.status_code == 302)

    create_response = client.post(f'/set-item-status/In Progress/{testing_consts["test_card_id"]}')
    assert(create_response.status_code == 302)

    create_response = client.post(f'/set-item-status/Complete/{testing_consts["test_card_id"]}')
    assert(create_response.status_code == 302)