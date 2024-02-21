import requests
import os

base_url = "https://api.trello.com/1"
#trello_board_id = "65d6337573a6275aed0ec68a" TODO: do I need this? - delete if not
trello_list_id="65d6362e050962e28cf00ae5"

def get_api_key():
    return "227ed8615e0f8b4a002244483db5ec7a"
    #return os.getenv('TRELLO_API_KEY')

def get_api_token():
    return "ATTA33185227669ef97599b66df3458fcd057fbc93771efa15e301c0f61c151d015e56F2752A"
    # os.getenv('TRELLO_API_TOKEN')

def display_error(response):
    print(f"ERROR: CODE {response.status_code} - {response.text}")

def map_card(card_response_json):
    # TODO: should be a todo item class instance, rather than a dict
    return {
        "id": card_response_json["id"],
        "title": card_response_json["name"],
        # TODO: status is currently in description - I want to allow cards to have descriptions, so it'd be good to find another way of storing status (maybe by having separate lists)
        "status": card_response_json["desc"],
    }

def get_cards():
    url = f"{base_url}/lists/{trello_list_id}/cards?key={get_api_key()}&token={get_api_token()}"

    response = requests.request("GET", url)
    
    
    if response.status_code >= 400:
        display_error(response)
        return None
    
    return list(map(map_card, response.json()))

def create_card(title):
    url = f"{base_url}/cards?idList={trello_list_id}&key={get_api_key()}&token={get_api_token()}"

    body = {
        "name": title,
        "desc": "Not Started"
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

#print(create_card("test"))
#print(get_cards())