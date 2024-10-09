import players
import settings as SETTINGS


class Game:
    def __init__(self) -> None:
        self.runner = players.Runner(clicks=SETTINGS.RUNNER_STARTING_CLICKS,
                                     credits=SETTINGS.RUNNER_STARTING_CREDITS,
                                     deck_size=SETTINGS.RUNNER_STARTING_DECK_SIZE,
                                     hand_size=SETTINGS.RUNNER_STARTING_HAND_SIZE)
        self.corp = players.Corp(clicks=SETTINGS.CORP_STARTING_CLICKS,
                                 credits=SETTINGS.CORP_STARTING_CREDITS,
                                 deck_size=SETTINGS.CORP_STARTING_DECK_SIZE,
                                 hand_size=SETTINGS.CORP_STARTING_HAND_SIZE)
        self.whos_turn: str = 'corp'

    def setup(self, runner_deck, corp_deck) -> None:
        self.runner.build_deck(runner_deck)
        self.corp.build_deck(corp_deck)
        self.runner.shuffle()
        self.corp.shuffle()

    def next_turn(self, player: players.Player):
        if player.clicks < 0:
            print('The ' + self.whos_turn + ' has used too many clicks.')
        if player.clicks <= 0:
            player.refresh_clicks()
            if self.whos_turn == 'corp':
                self.whos_turn = 'runner'
            else:
                self.whos_turn = 'corp'
            print('It is now the ' + self.whos_turn + '\'s turn.')
        else:
            print('It is still the ' + self.whos_turn + '\'s turn.')

    def start_of_turn(self):
        if self.whos_turn == 'corp':
            self.corp.draw(1, 0)

    def choose_action(self, player: players.Runner | players.Corp, action: str):
        name = type(player).__name__

        if action == 'draw':
            player.draw()
        if name == 'corp':
            player.start_run()
