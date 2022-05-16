from tinydb import TinyDB, Query


class Database:
    @staticmethod
    def get_db():
        db = TinyDB("db.json")
        return db

    @classmethod
    def get_user_table(cls):
        return cls.get_db().table("User")

    @classmethod
    def get_tournament_table(cls):
        return cls.get_db().table("Tournament")


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
            result = ([id_player, 0.5], 0.5)
            return result


class Round:
    def __init__(self):
        pass

    @classmethod
    def first_round(cls):
        pass

    @classmethod
    def normal_round(cls):
        pass


class Tournament:

    def __int__(self, tour_info):
        self.name = tour_info["Name"]
        self.place = tour_info["Place"]
        self.round_number = tour_info["Round Number"]
        self.time = tour_info["Time"]
        self.player_one = Player.read_player(tour_info["id1"])
        self.player_two = Player.read_player(tour_info["id2"])
        self.player_three = Player.read_player(tour_info["id3"])
        self.player_four = Player.read_player(tour_info["id4"])
        self.player_five = Player.read_player(tour_info["id5"])
        self.player_six = Player.read_player(tour_info["id6"])
        self.player_seven = Player.read_player(tour_info["id7"])
        self.player_eight = Player.read_player(tour_info["id8"])

    def lauch_tournament(self):
        Round.first_round()