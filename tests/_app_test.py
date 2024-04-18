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
    'test_card_name': 'Test card'
}

def stub(mode, url, params={}):
    if url == f'https://api.trello.com/1/boards/{get_board_id()}/cards?key={get_api_key()}&token={get_api_token()}':
        fake_response_data = [{'id': testing_consts['test_card_id'], 'name': testing_consts['test_card_name'], 'idList': get_not_started_list_id()}]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    @property
    def status_code(self):
        return 200

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
    monkeypatch.setattr(requests, 'request', stub)

    response = client.get('/')
    assert(response.status_code == 200)
    assert(testing_consts['test_card_id'] in response.data.decode())
    assert(testing_consts['test_card_name'] in response.data.decode())