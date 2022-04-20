class Player:
    def __init__(self, name, lastname, birthday, sex, classment):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.sex = sex
        self.classment = classment

    def save_to_db(self):
        pass

    def get_from_db(self):
        pass

    def delete_from_db(self):
        pass


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def game_result(self):
        pass


class Round:
    def __init__(self, game_one, game_two, game_three, game_four):
        self.game_one = game_one
        self.game_two = game_two
        self.game_three = game_three
        self.game_four = game_four

    def next_round(self):
        pass


class Tournament:
    def __init__(self, round_one, round_two, round_three, round_four):
        self.round_one = round_one
        self.round_two = round_two
        self.round_three = round_three
        self.round_four = round_four
