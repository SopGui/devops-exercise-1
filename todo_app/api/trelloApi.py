import requests
import os
import todo_app.api.todoItem as todoItem
import todo_app.api.trelloIds as trelloIds

base_url = "https://api.trello.com/1"

def get_list_id_from_status(status):
    if status == todoItem.TodoItemStatus.NOT_STARTED:
        return trelloIds.not_started_list_id
    if status == todoItem.TodoItemStatus.IN_PROGRESS:
        return trelloIds.in_progress_list_id
    if status == todoItem.TodoItemStatus.COMPLETE:
        return trelloIds.complete_list_id
    return "Unknown"

def get_status_from_list_id(list_id):
    if list_id == trelloIds.not_started_list_id:
        return todoItem.TodoItemStatus.NOT_STARTED
    if list_id == trelloIds.in_progress_list_id:
        return todoItem.TodoItemStatus.IN_PROGRESS
    if list_id == trelloIds.complete_list_id:
        return todoItem.TodoItemStatus.COMPLETE
    return None

def get_api_key():
    return os.getenv('TRELLO_API_KEY')

def get_api_token():
    return os.getenv('TRELLO_API_TOKEN')

def display_error(response):
    print(f"ERROR: CODE {response.status_code} - {response.text}")

def map_card(card_response_json):
    return todoItem.TodoItem(card_response_json["id"], card_response_json["name"], get_status_from_list_id(card_response_json["idList"]))

def get_cards():
    url = f"{base_url}/boards/{trelloIds.trello_board_id}/cards?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("GET", url)
    
    if response.status_code >= 400:
        display_error(response)
        return response.status_code

    cards = list(map(map_card, response.json()))
    cards = list(filter(lambda card : card.status != None, cards))
    cards.sort(key=lambda card : card.status)
    return cards

def create_card(title, status : todoItem.TodoItemStatus):
    list_id = get_list_id_from_status(status)
    url = f"{base_url}/cards?idList={list_id}&key={get_api_key()}&token={get_api_token()}"

    body = {
        "name": title,
    }

    response = requests.request("POST", url, data=body)

    if response.status_code >= 400:
        display_error(response)
        return None
    
    return response.status_code

def delete_card(card_id):
    print()
    url=f"{base_url}/cards/{card_id}?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("DELETE", url)

    if response.status_code >= 400:
        display_error(response)

    return response.status_code

def set_card_status(card_id, new_status: todoItem.TodoItemStatus):
    url=f"{base_url}/cards/{card_id}?key={get_api_key()}&token={get_api_token()}"

    body = {
        "idList": get_list_id_from_status(new_status),
    }

    response = requests.request("PUT", url, data=body)

    if response.status_code >= 400:
        display_error(response)
        return response.status_code

    return response.status_code