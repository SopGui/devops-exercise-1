import todo_app.api.todoItem as todoItem

class ListViewModel():
    def __init__(self, cards: list):
        self.id = id
        self.cards = cards

        #TODO put type checkig here
        
    def __str__(self):
        list_string = ""
        for card in self.cards:
            list_string = f"{list_string}\nCard - ID: {card.id} Title: {card.title}, Status: {card.status}"
        return list_string
        