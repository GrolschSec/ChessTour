import random

from tinydb import TinyDB
from datetime import datetime
from random import shuffle


class Database:
    @staticmethod
    def get_db():
        """
        This method load the database.
        Returns:
            db: The database.
        """
        db = TinyDB("db.json")
        return db

    @classmethod
    def get_user_table(cls):
        """
        The method load the "User" table of the database.
        Returns:
            cls.get_db().table("User"): The user table of the database.
        """
        return cls.get_db().table("User")

    @classmethod
    def user_id_exist(cls, identity):
        """
        The method is checking if a user id exist in the database.
        Args:
            identity: The user id to check.

        Returns:
            bool: The return value, True if the id exist, False if it doesn't.

        """
        db = cls.get_user_table()
        if db.get(doc_id=identity) is None:
            return False
        return True

    @classmethod
    def get_tournament_table(cls):
        """
        The method load the "Tournament" table of the database.
        Returns:
            cls.get_db().table("Tournament"): The user table of the database.
        """
        return cls.get_db().table("Tournament")

    @classmethod
    def get_round_table(cls):
        """
        The method load the "Round" Table.
        Returns:
            cls.get_db().table("Round"): the Round table.
        """
        return cls.get_db().table("Round")

    @classmethod
    def get_game_table(cls):
        """
        The method load the "Game" table.
        Returns:
            cls.get_db().table("Game"): The Game table.
        """
        return cls.get_db().table("Game")


class Player:
    """ """

    DB_USER = Database.get_user_table()

    def __init__(self, player_info):
        self.name = player_info["name"]
        self.lastname = player_info["lastname"]
        self.birthday = player_info["birthday"]
        self.sex = player_info["sex"]
        self.classment = player_info["classment"]
        self.point = 0

    def get_serialized_player(self):
        """
        The method take the player info and make it in a serialized format for the database.
        Returns:
            serialized_player: The dictionary containing the user info.
        """
        serialized_player = {
            "name": self.name,
            "lastname": self.lastname,
            "birthday": self.birthday,
            "sex": self.sex,
            "classment": self.classment,
        }
        return serialized_player

    def create_player(self):
        """
        The method save the data of a user in the database.
        Returns:
            void: Doesn't return anything.
        """
        player = self.get_serialized_player()
        self.DB_USER.insert(player)

    @classmethod
    def read_player(cls, identifier):
        """
        This method load a user from the database.
        Args:
            identifier: The user id of the player to load

        Returns:
            player: The instance of the player loaded.
        """
        return Player(cls.DB_USER.get(doc_id=identifier))

    @classmethod
    def update_player(cls, identifier, param, new_value):
        """
        The method permit to modify the information of a player from the database.
        Args:
            identifier: The user id of the user to modify.
            param: the parameter that you want to modify.
            new_value: the new value of the parameter.

        Returns:
            void: Doesn't return anything.

        """
        cls.DB_USER.update({param: new_value}, doc_ids=[identifier])

    @classmethod
    def delete_player(cls, identifier):
        """
        The method delete a user from the database.
        Args:
            identifier: The user id of the player you want to delete.

        Returns:
            void: Doesn't return anything.
        """
        cls.DB_USER.remove(doc_ids=[identifier])

    @classmethod
    def read_all_players(cls):
        """
        The method load all the players from the database.
        Returns:
            users: the list of all the users in the database.
            id_list: the list of all the ids of the players.
        """
        id_list = []
        users = cls.DB_USER.all()
        for i in range(0, len(users)):
            id_list.append(users[i].doc_id)
        return [users, id_list]


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def game_result(self, winner=int):
        """

        Args:
            winner: If equal to one mean player one is winner, if equal to two player two is winner,
            else game result is null.

        Returns:
            A tuple containing two list, the first with the instance of the player one and the results he got for the
            game and a second list with the data about the player two.
        """
        if winner == 1:
            result = ([self.player_one, 1], [self.player_two, 0])
            self.player_one.point += 1
        elif winner == 2:
            result = ([self.player_one, 0], [self.player_two, 1])
            self.player_two.point += 1
        else:
            result = ([self.player_one, 0.5], [self.player_two, 0.5])
            self.player_one.point += 0.5
            self.player_two.point += 0.5
        return result


class Round:
    def __init__(self, players):
        self.players = players
        self.games = []

    def first_round(self):
        """
        The method sort the players by their classment and then make four instance of games.
        Returns:
            games_round: the games instances for the round.
        """
        sort_players = sorted(
            self.players, reverse=True, key=lambda player: player.classment
        )
        games_round = []
        for i in range(0, 4):
            games_round.append(Game(sort_players[i], sort_players[i + 4]))
        return games_round

    def sort_player_by_point(self):
        games_round = []
        sort_players = sorted(
            self.players, reverse=True, key=lambda player: player.point
        )
        for i in range(0, 4):
            games_round.append(Game(sort_players[i], sort_players[i + 4]))
        return games_round

    def sort_player_random(self):
        games_round = []
        sort_players = sorted(self.players, key=lambda player: player.name)
        for i in range(0, 4):
            games_round.append(Game(sort_players[i], sort_players[i + 4]))
        return games_round

    def normal_round(self, *args):
        valid = False
        sort_players = self.sort_player_by_point()
        r = 0
        while r < len(args):
            i = 0
            while i < 4:
                if (
                    sort_players[i].player_one.name == args[r][i].player_one.name
                    and sort_players[i].player_one.lastname
                    == args[r][i].player_one.lastname
                    and sort_players[i].player_two.name == args[r][i].player_two.name
                    and sort_players[i].player_two.lastname
                    == args[r][i].player_two.lastname
                    or sort_players[i].player_one.name == args[r][i].player_two.name
                    and sort_players[i].player_one.lastname
                    == args[r][i].player_two.lastname
                    and sort_players[i].player_two.name == args[r][i].player_one.name
                    and sort_players[i].player_two.lastname
                    == args[r][i].player_one.lastname
                ):
                    valid = False
                    break
                else:
                    i += 1
                    valid = True
            if not valid:
                sort_players = self.sort_player_random()
                r = 0
            elif valid:
                r += 1
        return sort_players

    @staticmethod
    def round_result(games_result, games):
        i = 0
        res = []
        for game in games:
            res.append(game.game_result(games_result[i]))
            i += 1
        return res


class Tournament:
    DB_TOURNAMENT = Database.get_tournament_table()

    def __init__(self, tour_info):
        self.name = tour_info["Name"]
        self.place = tour_info["Place"]
        self.round_number = tour_info["Round Number"]
        self.gamestype = tour_info["Type of games"]
        self.begin_date_time = datetime.now()
        self.end_date_time = None
        self.players = []
        self.rounds = []
        self.is_done = False
        for i in range(1, 9):
            self.players.append(Player.read_player(tour_info[f"id{i}"]))

    def serialize(self):
        """

        Returns:

        """
        serialized_tournament = {
            "Name": self.name,
            "Place": self.place,
            "Number of rounds": self.round_number,
            "Type of games": self.gamestype,
            "Done": self.is_done,
        }
        return serialized_tournament

    def end_tournament(self):
        self.is_done = True
        self.end_date_time = datetime.now()
