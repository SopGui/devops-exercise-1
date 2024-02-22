import requests
import os
import todo_app.api.todoItemStatus as todoItemStatus
#import todoItemStatus

base_url = "https://api.trello.com/1"
trello_board_id = "65d6337573a6275aed0ec68a"
trello_list_id="65d6362e050962e28cf00ae5"

not_started_list_id="65d733960723c15693565524"
in_progress_list_id="65d7339b144d16a2cd686632"
complete_list_id="65d733a812de2dee30a1c327"

def get_list_id_from_status(status):
    if status == todoItemStatus.Todo_item_status.NOT_STARTED:
        return not_started_list_id
    elif status == todoItemStatus.Todo_item_status.IN_PROGRESS:
        return in_progress_list_id
    elif status == todoItemStatus.Todo_item_status.COMPLETE:
        return complete_list_id
    else:
        return "Unknown"

def get_status_from_list_id(list_id):
    if list_id == not_started_list_id:
        return todoItemStatus.Todo_item_status.NOT_STARTED
    elif list_id == in_progress_list_id:
        return todoItemStatus.Todo_item_status.IN_PROGRESS
    elif list_id == complete_list_id:
        return todoItemStatus.Todo_item_status.COMPLETE
    else:
        return None

# TODO : switch over to using environment varialbes before submitting
def get_api_key():
    #return "227ed8615e0f8b4a002244483db5ec7a"
    return os.getenv('TRELLO_API_KEY')

def get_api_token():
    #return "ATTA33185227669ef97599b66df3458fcd057fbc93771efa15e301c0f61c151d015e56F2752A"
    return os.getenv('TRELLO_API_TOKEN')

def display_error(response):
    print(f"ERROR: CODE {response.status_code} - {response.text}")

def map_card(card_response_json):
    # TODO: should be a todo item class instance, rather than a dict
    return {
        "id": card_response_json["id"],
        "title": card_response_json["name"],
        # TODO: status is currently in description - I want to allow cards to have descriptions, so it'd be good to find another way of storing status (maybe by having separate lists)
        "status": get_status_from_list_id(card_response_json["idList"]),
    }

def get_cards():
    url = f"{base_url}/boards/{trello_board_id}/cards?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("GET", url)
    
    if response.status_code >= 400:
        display_error(response)
        return None

    cards = list(map(map_card, response.json()))
    cards = list(filter(lambda card : card["status"] != None, cards))
    return cards

def create_card(title, status : todoItemStatus.Todo_item_status):
    list_id = get_list_id_from_status(status)
    url = f"{base_url}/cards?idList={list_id}&key={get_api_key()}&token={get_api_token()}"

    body = {
        "name": title,
    }

    response = requests.request("POST", url, data=body)

    if response.status_code >= 400:
        display_error(response)
        return None
    
    return map_card(response.json())

def delete_card(card_id):
    url=f"{base_url}/cards/{card_id}?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("DELETE", url)

    if response.status_code >= 400:
        display_error(response)

    return response.status_code

print(create_card("done", todoItemStatus.Todo_item_status.COMPLETE))
#print(get_cards())