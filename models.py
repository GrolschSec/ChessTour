from tinydb import TinyDB, Query


class Database:
    @staticmethod
    def get_db():
        db = TinyDB("db.json")
        return db

    @classmethod
    def get_user_table(cls):
        return cls.get_db().table("User")


class Player:
    DB_USER = Database.get_user_table()

    def __init__(self, player_info):
        self.name = player_info["name"]
        self.lastname = player_info["lastname"]
        self.birthday = player_info["birthday"]
        self.sex = player_info["sex"]
        self.classment = player_info["classment"]
        self.point = 0

    def get_serialized_player(self):
        serialized_player = {
            "name": self.name,
            "lastname": self.lastname,
            "birthday": self.birthday,
            "sex": self.sex,
            "classment": self.classment,
        }
        return serialized_player

    def create_player(self):
        player = self.get_serialized_player()
        self.DB_USER.insert(player)

    @classmethod
    def read_player(cls, identifier):
        return Player(cls.DB_USER.get(doc_id=identifier))

    @classmethod
    def update_player(cls, identifier, param, new_value):
        cls.DB_USER.update({param: new_value}, doc_ids=[identifier])

    @classmethod
    def delete_player(cls, identifier):
        cls.DB_USER.remove(doc_ids=[identifier])

    @classmethod
    def read_all_players(cls):
        id_list = []
        users = cls.DB_USER.all()
        for i in range(0, len(users)):
            id_list.append(users[i].doc_id)
        return [users, id_list]


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
