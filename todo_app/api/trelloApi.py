import requests
import os
import todo_app.api.todoItem as todoItem

base_url = "https://api.trello.com/1"
trello_board_id = "65d6337573a6275aed0ec68a"

not_started_list_id="65d733960723c15693565524"
in_progress_list_id="65d7339b144d16a2cd686632"
complete_list_id="65d733a812de2dee30a1c327"

def get_list_id_from_status(status):
    if status == todoItem.TodoItemStatus.NOT_STARTED:
        return not_started_list_id
    if status == todoItem.TodoItemStatus.IN_PROGRESS:
        return in_progress_list_id
    if status == todoItem.TodoItemStatus.COMPLETE:
        return complete_list_id
    return "Unknown"

def get_status_from_list_id(list_id):
    if list_id == not_started_list_id:
        return todoItem.TodoItemStatus.NOT_STARTED
    if list_id == in_progress_list_id:
        return todoItem.TodoItemStatus.IN_PROGRESS
    if list_id == complete_list_id:
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
    url = f"{base_url}/boards/{trello_board_id}/cards?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("GET", url)
    
    if response.status_code >= 400:
        display_error(response)
        return response.status_code

    cards = list(map(map_card, response.json()))
    cards = list(filter(lambda card : card.status != None, cards))
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

    print(response.status_code)    
    print(response.text)

    if response.status_code >= 400:
        display_error(response)

    return response.status_code

def set_card_status(card_id, new_status: todoItem.TodoItemStatus):
    url=f"{base_url}/cards/{card_id}?key={get_api_key()}&token={get_api_token()}"

    body = {
        "idList": get_list_id_from_status(new_status),
    }

    print(new_status)
    print(body)

    response = requests.request("PUT", url, data=body)

    print(response.text)

    if response.status_code >= 400:
        display_error(response)
        return response.status_code

    return response.status_code