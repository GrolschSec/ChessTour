from tinydb import TinyDB
import time

class Database:
    @staticmethod
    def get_db():
        db = TinyDB("db.json")
        return db

    @classmethod
    def get_user_table(cls):
        return cls.get_db().table("User")

    @classmethod
    def user_id_exist(cls, identity):
        db = cls.get_user_table()
        if db.get(doc_id=identity) is None:
            return False
        return True

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
            result = ([self.player_one, 1], [self.player_two, 0])
            return result
        elif winner == self.player_two:
            result = ([self.player_one, 0], [self.player_two, 1])
            return result
        else:
            result = ([self.player_one, 0.5], [self.player_two, 0.5])
            return


class Round:
    def __init__(self, players, time):
        self.players = players
        self.time = time

    def sort_round_one(self):
        sorted_players = sorted(self.players, key=lambda player: player.classment)
        sorted_players.reverse()
        games_round = []
        for i in range(0, 4):
            games_round.append(Game(sorted_players[i], sorted_players[i + 4]))
        return games_round

    def first_round(self):
        games = self.sort_round_one()
        for game in games:



    @classmethod
    def normal_round(cls):
        pass


class Tournament:
    def __init__(self, tour_info):
        self.name = tour_info["Name"]
        self.place = tour_info["Place"]
        self.round_number = tour_info["Round Number"]
        self.time = tour_info["Time"]
        self.players = []
        for i in range(1, 9):
            self.players.append(Player.read_player(tour_info[f"id{i}"]))

    def launch_tournament(self):
        rounds = Round(self.players, self.time)
        rounds.first_round()
        while self.round_number - 1 < 0:
            rounds.normal_round()
            self.round_number -= 1
