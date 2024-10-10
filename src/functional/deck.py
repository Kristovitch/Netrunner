import json
import random
import utils
import card


class Deck:
    '''
    '''
    def __init__(self, name: str = '', deck_type: str = '') -> None:
        '''
        Blah
        '''
        self.name: str = name
        self.deck_type: str = deck_type
        self.identity_card: card.Card = None
        self.cards: list[card.Card] = []

    def load_deck(self, deck_list_file: str):
        '''
        Load a deck from a list of cards.
        Currently supports JSON files.
        Parameters
        ----------
        deck_list_file: str
            The dictionary object containing strings that are to be concatinated.

        Returns
        ----------
        str
        The concatinated string.
        '''
        with open(deck_list_file, 'r', encoding='utf-8') as deck_list:
            deck_list = json.load(deck_list)

        self.deck_type = deck_list['type']
        self.identity_card = deck_list['identity_card']
        for x in deck_list['cards']:
            self.cards.append(utils.create_card[x])
        self.shuffle()

    def shuffle(self):
        '''
        Randomise the order of cards in a deck
        '''
        random.random(self.cards)
