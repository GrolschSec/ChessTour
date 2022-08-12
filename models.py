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
    DB_USER = Database.get_user_table()

    def __init__(self, player_info):
        self.id = None
        self.name = player_info["name"]
        self.lastname = player_info["lastname"]
        self.birthday = player_info["birthday"]
        self.sex = player_info["sex"]
        self.classment = player_info["classment"]
        self.point = 0
        self.opponents = []

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

    def clear_opponents(self):
        self.opponents = []

    def create(self):
        """
        The method save the data of a user in the database.
        Returns:
            void: Doesn't return anything.
        """
        self.id = self.DB_USER.insert(self.serialize())

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
        player.id = identifier
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

    def read_tour_info(self):
        self.point = self.DB_USER.get(doc_id=self.id)["point"]
        self.opponents = self.DB_USER.get(doc_id=self.id)["opponents"]


class Game:
    DB_GAME = Database.get_game_table()

    def __init__(self, player_one, player_two):
        self.id = int
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
                    f"[{self.player_one.id}] {self.player_one.name} {self.player_one.lastname}",
                    1,
                ],
                [
                    f"[{self.player_two.id}] {self.player_two.name} {self.player_two.lastname}",
                    0,
                ],
            )
            self.player_one.point += 1
        elif winner == 2:
            result = (
                [
                    f"[{self.player_one.id}] {self.player_one.name} {self.player_one.lastname}",
                    0,
                ],
                [
                    f"[{self.player_two.id}] {self.player_two.name} {self.player_two.lastname}",
                    1,
                ],
            )
            self.player_two.point += 1
        else:
            result = (
                [
                    f"[{self.player_one.id}] {self.player_one.name} {self.player_one.lastname}",
                    0.5,
                ],
                [
                    f"[{self.player_two.id}] {self.player_two.name} {self.player_two.lastname}",
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
        self.id = int
        self.players = players
        self.p_selected = []
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
            self.players[i].opponents.append(self.players[i + 4].id)
            self.players[i + 4].opponents.append(self.players[i].id)
            self.games.append(Game(self.players[i], self.players[i + 4]))

    def select_p1(self):
        p1 = None
        for i in range(0, 8):
            if self.players[i].id not in self.p_selected:
                self.p_selected.append(self.players[i].id)
                p1 = self.players[i]
                break
        return p1

    def select_p2(self, p1):
        p2 = None
        for i in range(0, 8):
            if (
                self.players[i].id not in self.p_selected
                and self.players[i].id not in p1.opponents
            ):
                self.p_selected.append(self.players[i].id)
                p2 = self.players[i]
                p2.opponents.append(p1.id)
                p1.opponents.append(p2.id)
                break
        return p2

    def sort_by_point(self):
        sorted(self.players, reverse=True, key=lambda player: player.point)
        while len(self.games) != 4:
            p1 = self.select_p1()
            p2 = self.select_p2(p1)
            self.games.append(Game(p1, p2))

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
        self.id = None
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
        self.id = self.DB_TOURNAMENT.insert(self.serialize())
        return self.id

    @classmethod
    def read(cls, identifier):
        tournament = Tournament(cls.DB_TOURNAMENT.get(doc_id=identifier))
        tournament.id = identifier
        return tournament

    def end_tournament(self):
        self.is_done = True
        self.end_date_time = f"{datetime.now()}"
        self.DB_TOURNAMENT.update({"is_done": self.is_done}, doc_ids=[self.id])
        self.DB_TOURNAMENT.update(
            {"end_date_time": self.end_date_time}, doc_ids=[self.id]
        )

    def sort_round(self, i):
        round_r = Round(self.players)
        if i == 0:
            round_r.sort_by_classment()
        elif 0 < i < 8:
            round_r.sort_by_point()
        elif i > 7:
            for player in self.players:
                player.clear_opponents()
            round_r.sort_by_point()
        return round_r

    def save_players_data(self):
        for player in self.players:
            player.update(player.id, "point", player.point)
            player.update(player.id, "opponents", player.opponents)

    def load_players_data(self):
        for player in self.players:
            player.read_tour_info()

    def get_i(self):
        i = -1
        for key in self.DB_TOURNAMENT.get(doc_id=self.id).keys():
            word = key.split("_")
            if "round" in word:
                i += 1
        return i

    def save_round(self, round_r, round_res):
        identifier = round_r.save(round_res)
        self.DB_TOURNAMENT.update({"round": identifier}, doc_ids=[self.id])
