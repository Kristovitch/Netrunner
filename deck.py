import json
import utils
import card


class Deck:
    '''
    '''
    def __init__(self, name: str = '', deck_type: str = '') -> None:
        '''
        Blah
        '''
        self.name:str = name
        self.deck_type:str = deck_type
        self.identity_card:card.Card = None
        self.cards:list[card.Card] = []

    def load_deck(self, deck_list_file):
        '''
        
        '''
        with open(deck_list_file, 'r', encoding='utf-8') as deck_list:
            deck_list = json.load(deck_list)

        self.deck_type = deck_list['type']
        self.identity_card = deck_list['identity_card']
        for x in deck_list['cards']:
            self.cards.append(utils.create_card[x])
