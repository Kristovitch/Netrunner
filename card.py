class Card:
    def __init__(self, title, subtitle='', faction='', play_cost=0,
                 card_type='', card_subtype='', card_text='', min_deck_size=0,
                 strength=0, influence_value=0, influence_limit=0, set_info=''
                 ) -> None:
        self.title = title
        self.subtitle = subtitle
        self.faction = faction
        self.play_cost = play_cost
        self.card_type = card_type
        self.card_subtype = card_subtype
        self.card_text = card_text
        self.min_deck_size = min_deck_size
        self.strength = strength
        self.influence_value = influence_value
        self.influence_limit = influence_limit
        self.set_info = set_info

    @classmethod
    def from_dict(self, card_data: dict) -> None:
        self.title = card_data['title']
        self.subtitle = card_data['subtitle']
        self.faction = card_data['faction']
        self.play_cost = card_data['play_cost']
        self.card_type = card_data['card_type']
        self.card_subtype = card_data['card_subtype']
        self.card_text = card_data['card_text']
        self.min_deck_size = card_data['min_deck_size']
        self.strength = card_data['strength']
        self.influence_value = card_data['influence_value']
        self.influence_limit = card_data['influence_limit']
        self.set_info = card_data['set_info']


class RunnerCard(Card):
    def __init__(self, title, subtitle='', faction='', play_cost=0,
                 card_type='', card_subtype='', card_text='', min_deck_size=0,
                 strength=0, influence_value=0, influence_limit=0, set_info='',
                 base_link='', install_cost=0, memory_cost=0) -> None:
        super().__init__(title, subtitle, faction, play_cost,
                         card_type, card_subtype, card_text, min_deck_size,
                         strength, influence_value, influence_limit, set_info)
        self.base_link = base_link
        self.install_cost = install_cost
        self.memory_cost = memory_cost

    @classmethod
    def from_dict(self, card_data: dict) -> None:
        super().from_dict(card_data)
        self.base_link = card_data['base_link']
        self.install_cost = card_data['install_cost']
        self.memory_cost = card_data['memory_cost']


class CorpCard(Card):
    def __init__(self, title, subtitle='', faction='', play_cost=0,
                 card_type='', card_subtype='', card_text='', min_deck_size=0,
                 strength=0, influence_value=0, influence_limit=0, set_info='',
                 advancement_requerement='', agenda_points=0, rez_cost=0,
                 trash_cost=0) -> None:
        super().__init__(title, subtitle, faction, play_cost,
                         card_type, card_subtype, card_text, min_deck_size,
                         strength, influence_value, influence_limit, set_info)
        self.advancement_requerement = advancement_requerement
        self.agenda_points = agenda_points
        self.rez_cost = rez_cost
        self.trash_cost = trash_cost

    @classmethod
    def from_dict(self, card_data: dict) -> None:
        super().from_dict(card_data)
        self.advancement_requerement = card_data['advancement_requerement']
        self.agenda_points = card_data['agenda_points']
        self.rez_cost = card_data['rez_cost']
        self.trash_cost = card_data['trash_cost']
