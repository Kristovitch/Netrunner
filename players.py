import random


class Player:
    def __init__(self, clicks=0, credits=0,
                 identity='', deck_size=0, hand_size=0) -> None:
        self.clicks = clicks
        self.max_clicks = clicks
        self.credits = credits
        self.score = 0
        self.identity = identity
        self.deck_size = deck_size
        self.hand_size = hand_size
        self.deck = [] * self.deck_size
        self.hand = [] * self.hand_size
        self.graveyard = []

    def refresh_clicks(self) -> None:
        '''
        Reset the number of clicks to the maximum.

        Parameters
        ----------
        None

        Returns
        ----------
        None

        Raises
        ----------
        None
        '''
        self.clicks = self.max_clicks

    def use_clicks(self, number_of_clicks_used: int) -> bool:
        '''
        Checks if the number of clicks is availble to use.
        If it is, deduct that number of clicks from the remaining click pool.

        Parameters
        ----------
        number_of_clicks_used: int
            The number of clicks that are to be spent.

        Returns
        ----------
        bool
            Will return True if the clicks are spent.
            Will return False if there are not enough clicks to spend.

        Raises
        ----------
        None
        '''
        if number_of_clicks_used > self.clicks:
            print('Not enough clicks. Cost: ', number_of_clicks_used,
                  ' Credits: ', self.clicks)
            return False
        else:
            self.clicks -= number_of_clicks_used
            print('Spent ', number_of_clicks_used, ' clicks')
            return True

    def use_credits(self, number_of_credits_used: int) -> bool:
        '''
        Checks if the number of credits is availble to use.
        If it is, deduct that number of credits from the players credits.

        Parameters
        ----------
        number_of_credits_used: int
            The number of credits that are to be spent.

        Returns
        ----------
        bool
            Will return True if the credits are spent.
            Will return False if there are not enough credits to spend.

        Raises
        ----------
        None
        '''
        if number_of_credits_used > self.credits:
            print('Not enough credits. Cost: ', number_of_credits_used,
                  ' Credits: ', self.credits)
            return False
        else:
            self.credits -= number_of_credits_used
            print('Spent ', number_of_credits_used, ' credits')
            return True

    def gain_credits(self, number_of_credits_gained: int,
                     click_cost: int = 0) -> bool:
        '''
        Spends a number of clicks to gain a number of credits.
        If the number of credits spent to gain clicks is unavailable,
        the credits will not be gained.

        Parameters
        ----------
        number_of_credits_gained: int
            The number of credits that are to be gained.

        click_cost: int = 0
            The number of clicks to spend to gain those credits.

        Returns
        ----------
        bool
            Will return True if the credits are gained.
            Will return False if there are not enough clicks to spend.

        Raises
        ----------
        None
        '''
        if self.use_click(click_cost):
            self.credits += number_of_credits_gained
            return True
        else:
            return False

    def draw(self, number_of_cards_to_draw, click_cost: int = 0):
        '''
        Draw cards from a deck into a hand.
        '''
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
    def __init__(self, clicks: int = 4, credits: int = 0, identity: str = '',
                 deck_size: int = 0, hand_size: int = 5):
        '''
        Runner player constrcutor.

        Parameters
        ----------
        clicks: int = 4
            Starting number of clicks for the runner.

        credits: int = 0
            Starting number of credits.

        identity: str = ''
            Starting identity of the player.

        deck_size: int = 0
            The max deck size for the player.

        hand_size: int = 5
            The max hand size for the player.
        '''
        super().__init__(clicks, credits, identity, deck_size, hand_size)

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
    def __init__(self, clicks=3, credits=0, identity='', deck_size=0,
                 hand_size=5):
        super().__init__(clicks, credits, identity, deck_size, hand_size)

    def install_card(self, card):
        pass

    def play_operation(self, card):
        pass

    def trash_runner_resource(self, resource):
        if self.use_credits(2) and self.use_click(1):
            print(resource, ' has been trashed.')

    def trigger_ability(self, card):
        pass
