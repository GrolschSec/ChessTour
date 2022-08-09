from tinydb import TinyDB
from datetime import datetime


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
        self.pid = int
        self.name = player_info["name"]
        self.lastname = player_info["lastname"]
        self.birthday = player_info["birthday"]
        self.sex = player_info["sex"]
        self.classment = player_info["classment"]
        self.point = 0

    def serialize(self):
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

    def create(self):
        """
        The method save the data of a user in the database.
        Returns:
            void: Doesn't return anything.
        """
        self.pid = self.DB_USER.insert(self.serialize())

    @classmethod
    def read(cls, identifier):
        """
        This method load a user from the database.
        Args:
            identifier: The user id of the player to load

        Returns:
            player: The instance of the player loaded.
        """
        player = Player(cls.DB_USER.get(doc_id=identifier))
        player.pid = identifier
        return player

    @classmethod
    def update(cls, identifier, param, new_value):
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
    def delete(cls, identifier):
        """
        The method delete a user from the database.
        Args:
            identifier: The user id of the player you want to delete.

        Returns:
            void: Doesn't return anything.
        """
        cls.DB_USER.remove(doc_ids=[identifier])

    @classmethod
    def read_all(cls):
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
    DB_GAME = Database.get_game_table()

    def __init__(self, player_one, player_two):
        self.gid = int
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
            result = (
                [
                    f"[{self.player_one.pid}] {self.player_one.name} {self.player_one.lastname}",
                    1,
                ],
                [
                    f"[{self.player_two.pid}] {self.player_two.name} {self.player_two.lastname}",
                    0,
                ],
            )
            self.player_one.point += 1
        elif winner == 2:
            result = (
                [
                    f"[{self.player_one.pid}] {self.player_one.name} {self.player_one.lastname}",
                    0,
                ],
                [
                    f"[{self.player_two.pid}] {self.player_two.name} {self.player_two.lastname}",
                    1,
                ],
            )
            self.player_two.point += 1
        else:
            result = (
                [
                    f"[{self.player_one.pid}] {self.player_one.name} {self.player_one.lastname}",
                    0.5,
                ],
                [
                    f"[{self.player_two.pid}] {self.player_two.name} {self.player_two.lastname}",
                    0.5,
                ],
            )
            self.player_one.point += 0.5
            self.player_two.point += 0.5
        return result

    def save(self, winner):
        result = self.game_result(winner)
        return self.DB_GAME.insert({"game": result})


class Round:
    DB_ROUND = Database.get_round_table()

    def __init__(self, players):
        self.rid = int
        self.players = players
        self.games = []

    def sort_by_classment(self):
        """
        The method sort the players by their classment and then make four instance of games.
        Returns:
            games_round: the games instances for the round.
        """
        self.games = []
        sorted(self.players, reverse=True, key=lambda player: player.classment)
        for i in range(0, 4):
            self.games.append(Game(self.players[i], self.players[i + 4]))
        return self.games

    def sort_by_point(self):
        self.games = []
        sorted(self.players, reverse=True, key=lambda player: player.point)
        i = 0
        while i < 8:
            self.games.append(Game(self.players[i], self.players[i + 1]))
            i += 2
        return self.games

    @staticmethod
    def compare_game(old_game, new_game):
        if (
            new_game.player_one.pid == old_game.player_one.pid
            and new_game.player_two.pid == old_game.player_two.pid
        ):
            return False
        elif (
            new_game.player_one.pid == old_game.player_two.pid
            and new_game.player_two.pid == old_game.player_one.pid
        ):
            return False
        return True

    @classmethod
    def compare_round(cls, old_round, new_round):
        j = 0
        while j < 4:
            for i in range(0, 4):
                if not cls.compare_game(old_round[i], new_round[j]):
                    return False
            j += 1
        return True

    @classmethod
    def regular_round(cls, *args):
        sort_players = cls.sort_by_point()
        i = 0
        while i < len(args):
            if not cls.compare_round(args[i], sort_players):
                sort_players = None
                i = 0
            elif cls.compare_round(args[i], sort_players):
                i += 1
        return sort_players

    def save(self, games_result):
        i = 0
        res = {}
        for game in self.games:
            identifier = game.save(games_result[i])
            res.update({f"Game {i + 1}": identifier})
            i += 1
        return self.DB_ROUND.insert(res)


class Tournament:
    DB_TOURNAMENT = Database.get_tournament_table()

    def __init__(self, tour_info):
        self.tid = int
        self.name = tour_info["name"]
        self.location = tour_info["location"]
        self.gamestype = tour_info["time_control"]
        self.round_number = tour_info["round_number"]
        self.description = tour_info["description"]
        self.begin_date_time = f"{datetime.now()}"
        self.end_date_time = None
        self.player_ids = tour_info["player_ids"]
        self.is_done = False
        self.players = []
        for ids in tour_info["player_ids"]:
            self.players.append(Player.read(ids))

    def serialize(self):
        """

        Returns:

        """
        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "time_control": self.gamestype,
            "round_number": self.round_number,
            "description": self.description,
            "player_ids": self.player_ids,
            "begin_date_time": self.begin_date_time,
            "end_date_time": self.end_date_time,
            "is_done": self.is_done,
        }
        return serialized_tournament

    def create(self):
        self.tid = self.DB_TOURNAMENT.insert(self.serialize())
        return self.tid

    @classmethod
    def read(cls, identifier):
        tournament = Tournament(cls.DB_TOURNAMENT.get(doc_id=identifier))
        tournament.tid = identifier
        return tournament

    def end_tournament(self):
        self.is_done = True
        self.end_date_time = f"{datetime.now()}"
        self.DB_TOURNAMENT.update({"is_done": self.is_done}, doc_ids=self.tid)
        self.DB_TOURNAMENT.update({"end_date_time": self.end_date_time}, doc_ids=self.tid)

    def sort_round(self, i):
        round_r = Round(self.players)
        if i == 0:
            round_r.sort_by_classment()
        elif 0 < i < 4:
            round_r.sort_by_point()
        else:
            round_r.sort_by_point()
        return round_r

    def save_round(self, round_r, round_res, i):
        identifier = round_r.save(round_res)
        self.DB_TOURNAMENT.update({f"Round {i}": identifier}, doc_ids=[self.tid])
