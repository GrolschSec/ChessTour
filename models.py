class Player:
    def __init__(self, player_info):
        self.name = player_info['name']
        self.lastname = player_info['lastname']
        self.birthday = player_info['birthday']
        self.sex = player_info['sex']
        self.classment = player_info['classment']
        self.point = 0

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

    def game_result(self, winner):
        if winner == self.player_one:
            result = (1, 0)
            return result
        elif winner == self.player_two:
            result = (0, 1)
            return result
        else:
            result = (0.5, 0.5)
            return result


class Round:
    def __init__(self, game_one, game_two, game_three, game_four):
        self.game_one = game_one
        self.game_two = game_two
        self.game_three = game_three
        self.game_four = game_four

    def first_round(self):
        pass

    def normal_round(self):
        pass


class Tournament:
    def __init__(self, round_one, round_two, round_three, round_four):
        self.round_one = round_one
        self.round_two = round_two
        self.round_three = round_three
        self.round_four = round_four
