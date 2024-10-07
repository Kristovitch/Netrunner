import random


class Player:
    def __init__(self, clicks=0, credits=0, score=0,
                 identity='', deck_size=0, hand_size=0) -> None:
        self.clicks = clicks
        self.max_clicks = clicks
        self.credits = credits
        self.score = score
        self.identity = identity
        self.deck_size = deck_size
        self.hand_size = hand_size
        self.deck = [] * self.deck_size
        self.hand = [] * self.hand_size
        self.graveyard = []

    def refresh_clicks(self):
        self.clicks = self.max_clicks

    def use_click(self, number_of_clicks_used: int):
        if number_of_clicks_used > self.clicks:
            print('Not enough clicks. Cost: ', number_of_clicks_used, ' Credits: ', self.clicks)
        else:
            self.clicks -= number_of_clicks_used
            print('Spent ', number_of_clicks_used, ' clicks')
            return True

    def use_credits(self, number_of_credits_used: int) -> bool:
        if number_of_credits_used > self.credits:
            print('Not enough credits. Cost: ', number_of_credits_used, ' Credits: ', self.credits)
            return False
        else:
            self.credits -= number_of_credits_used
            print('Spent ', number_of_credits_used, ' credits')
            return True

    def gain_credits(self, number_of_credits_gained: int, click_cost: int = 0):
        if self.use_click(click_cost):
            self.credits += number_of_credits_gained

    def draw(self, number_of_cards_to_draw, click_cost: int = 0):
        if self.use_clicks(click_cost):
            pass

    # May need to rebuild this function if card logic changes.
    def discard(self, card):
        for dict_ in self.hand:
            if dict_ == card:
                self.graveyard.append(card)
                self.hand.remove(card)
                print(card['title'], ' has been sent to the graveyard.')
                return True
        return False

    def build_deck(self, cardlist: dict):
        pass

    def shuffle(self):
        random.shuffle(self.deck)


class Runner(Player):
    def __init__(self, clicks=4, credits=0, score=0,
                 identity='', deck_size=0, hand_size=5):
        super().__init__(clicks, credits, score,
                         identity, deck_size, hand_size)

    def install_card(self, card):
        pass

    def play_event(self, card):
        pass

    def add_tag(self):
        pass

    def remove_tag(self, tag):
        pass

    def trigger_ability(self, card):
        pass

    def start_run(self):
        pass


class Corp(Player):
    def __init__(self, clicks=3, credits=0, score=0,
                 identity='', deck_size=0, hand_size=5):
        super().__init__(clicks, credits, score,
                         identity, deck_size, hand_size)

    def install_card(self, card):
        pass

    def play_operation(self, card):
        pass

    def trash_runner_resource(self, resource):
        if self.use_credits(2) and self.use_click(1):
            print(resource, ' has been trashed.')

    def trigger_ability(self, card):
        pass
