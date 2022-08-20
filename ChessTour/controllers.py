from models import Player, Tournament, Database, Round, Game
from views import MenuView
from sys import exit


class MenuController:
    MENU_VIEW = MenuView()

    @classmethod
    def run(cls):
        """
        This method run the main menu.
        Returns:
            void
        """
        while True:
            menu_choice = cls.MENU_VIEW.display_main()
            if menu_choice == 1:
                cls.run_player()
            elif menu_choice == 2:
                cls.run_tournament()
            elif menu_choice == 3:
                cls.quit_program()
            else:
                cls.MENU_VIEW.max_input(3)

    @classmethod
    def run_player(cls):
        """
        This method run the player menu.
        Returns:
            void.
        """
        while True:
            menu_choice = cls.MENU_VIEW.display_player()
            if menu_choice == 1:
                Player(cls.MENU_VIEW.add_player()).create()
            elif menu_choice == 2:
                cls.show_players(0)
                player_id = cls.check_id(cls.MENU_VIEW.ID_MODIFY)
                player_info = Player.read(player_id)
                player_update = cls.MENU_VIEW.modify_player(
                    player_id, player_info.serialize()
                )
                Player.update(player_update[0], player_update[1], player_update[2])
            elif menu_choice == 3:
                cls.show_players(0)
                id_player = cls.check_id(cls.MENU_VIEW.ID_REMOVE)
                if cls.MENU_VIEW.delete_player():
                    Player.delete(id_player)
                    cls.MENU_VIEW.player_deleted()
            elif menu_choice == 4:
                cls.show_players(0)
            elif menu_choice == 5:
                break
            else:
                cls.MENU_VIEW.max_input(5)

    @classmethod
    def run_tournament(cls):
        """
        This method run the tournament menu.
        Returns:
            void.
        """
        while True:
            menu_choice = cls.MENU_VIEW.display_tournament()
            if menu_choice == 1:
                i = 0
                tournament = Tournament(cls.tournament_info())
                cls.tournament(tournament, i)
            elif menu_choice == 2:
                id_tournament = cls.select_tournament("u")
                if id_tournament:
                    tournament = Tournament.read(id_tournament)
                    i = tournament.get_i()
                    cls.tournament(tournament, i)
            elif menu_choice == 3:
                cls.run_reports()
            elif menu_choice == 4:
                break
            else:
                cls.MENU_VIEW.max_input(4)

    @classmethod
    def check_id(cls, message):
        """
        This function check if an id exist or not in the database.
        Args:
            message: a personalized message to show.

        Returns:
            identifier: if it exist it return the id.
        """
        identifier = int
        while True:
            try:
                identifier = cls.MENU_VIEW.id(message)
                if not Database.id_exist(identifier, 1):
                    raise ValueError
            except ValueError:
                cls.MENU_VIEW.id_error(1)
                continue
            break
        return identifier

    @classmethod
    def show_players(cls, m):
        """
        This function show the list of all players registered in the database.
        """
        if m == 0:
            cls.MENU_VIEW.show_all_player(Player.read_all(2))
        elif m == 1:
            cls.MENU_VIEW.show_all_player(Player.read_all(0))
        elif m == 2:
            cls.MENU_VIEW.show_all_player(Player.read_all(1))

    @classmethod
    def quit_program(cls):
        """
        This function exit the program properly.
        """
        cls.MENU_VIEW.quit_program()
        exit(0)

    @classmethod
    def select_tournament(cls, t):
        """
        This function is used to select a tournament to continue, or to show a report.
        Args:
            t: the type of tournament unfinished, or finished.

        Returns:
            the id of the selected tournament.
        """
        identifier = 0
        tournaments = Tournament.load(True)
        if t == "u":
            tournaments = Tournament.load(False)
        if not tournaments[0]:
            cls.MENU_VIEW.nothing_to_continue()
            return
        while True:
            try:
                if t == "u":
                    identifier = cls.MENU_VIEW.show_u_tournaments(tournaments[0])
                else:
                    identifier = cls.MENU_VIEW.show_f_tournaments(tournaments[0])
                if identifier == 99:
                    return
                elif (
                    not Database.id_exist(identifier, 2)
                    or identifier not in tournaments[1]
                ):
                    raise ValueError
            except ValueError:
                cls.MENU_VIEW.id_error(1)
                continue
            break
        return identifier

    @classmethod
    def tournament_info(cls):
        """
        This function get the info of the tournament
        (Name, place, number of rounds, type of games, and the players instances).
        Returns:
            tour_info: a dictionary that contains all the tournament information.
        """
        tour_info = cls.MENU_VIEW.tournament_info()
        id_list = []
        cls.show_players(0)
        for i in range(1, 9):
            identifier = cls.user_selected(id_list)
            id_list.append(identifier)
        tour_info.update({"player_ids": id_list})
        return tour_info

    @classmethod
    def tournament(cls, tournament, i):
        """
        This method is the algorithm of the tournament
        Args:
            tournament: the Tournament instance
            i: the index of the tournament.

        Returns:
            void.
        """
        if i == 0 and tournament.id is None:
            if cls.MENU_VIEW.save_to_db():
                tournament.create()
            else:
                return
        if cls.MENU_VIEW.tournament_msg(i):
            if i > 0:
                tournament.load_players_data()
            while i < int(tournament.round_number):
                round_r = tournament.sort_round(i)
                cls.round_or_classment(tournament)
                cls.MENU_VIEW.show_games(round_r.games)
                if cls.MENU_VIEW.play_the_round():
                    round_res = cls.MENU_VIEW.game_win(round_r.games)
                    round_r.append_opponents()
                    tournament.save_round(round_r, round_res, i)
                    i += 1
                else:
                    tournament.save_players_data()
                    return
            tournament.clear_players_data()
            tournament.end()
            cls.MENU_VIEW.end_tournament()

    @classmethod
    def user_selected(cls, id_list):
        """
        Check if a user is already selected or not.
        Args:
            id_list: the list of identifier.

        Returns:
            The identifier of the user if correct.
        """
        identifier = 0
        while True:
            try:
                identifier = cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)
                if identifier in id_list:
                    raise ValueError
            except ValueError:
                cls.MENU_VIEW.id_error(2)
                continue
            break
        return identifier

    @classmethod
    def run_reports(cls):
        """
        This function show the report menu.
        """
        while True:
            choice = cls.MENU_VIEW.display_reports()
            if choice == 1:
                user_report = cls.MENU_VIEW.users_report()
                if user_report == 1:
                    cls.show_players(1)
                elif user_report == 2:
                    cls.show_players(2)
            elif choice == 2:
                round_info = None
                tour_id = cls.select_tournament("f")
                if tour_id:
                    round_info = cls.tournament_report(tour_id)
                if round_info != 0:
                    cls.round_report(round_info)
            elif choice == 3:
                break
            else:
                cls.MENU_VIEW.max_input(3)

    @staticmethod
    def in_dict(n, round_dict):
        """
        This method check if a value is present in a dictionary.
        Args:
            n: the value
            round_dict: the dictionary.

        Returns:
            True if the value  is present, False if not.
        """
        for key in round_dict:
            if n == round_dict[f"{key}"]:
                return True
        return False

    @classmethod
    def tournament_report(cls, tour_id):
        """
        Make a report of the tournament !
        Args:
            tour_id: the id of the tournament

        Returns:
            void.
        """
        tournament = Tournament.read(tour_id)
        round_dict = tournament.rounds_from_db()
        option = cls.MENU_VIEW.tournament_report(tournament, round_dict)
        if option == 1:
            choice = cls.MENU_VIEW.select_players_view()
            if choice == 1:
                tournament.sort_players_alphabet()
                cls.MENU_VIEW.show_players_tournament(tournament)
            elif choice == 2:
                tournament.sort_players_classment()
                cls.MENU_VIEW.show_players_tournament(tournament)
            return 0
        elif option == 2:
            return cls.info_round(round_dict)

    @classmethod
    def info_round(cls, round_dict):
        """
        Ask for which round the user wants to see.
        Args:
            round_dict: the rounds info

        Returns:
            a list with the round id and the round name or 0 if we quit
        """
        n = None
        while True:
            try:
                n = cls.MENU_VIEW.round_id()
                if n == 99:
                    return 0
                if not cls.in_dict(n, round_dict):
                    raise ValueError
            except ValueError:
                continue
            break
        return [n, [k for k, v in round_dict.items() if v == n]]

    @classmethod
    def round_report(cls, round_info):
        """
        Make a report of the round.
        Args:
            round_info: the round information.

        Returns:
            void.
        """
        round_dict = Round.games_from_db(round_info[0])
        games_ids = []
        for keys in round_dict.keys():
            word = keys.split(" ")
            if "Game" in word:
                games_ids.append(round_dict[keys])
        games = Game.load_games_res(games_ids)
        round_name = round_info[1][0]
        players_one = []
        players_two = []
        for game in games:
            players_one.append(Player.read(list(game.items())[0][1][0][0][0]))
            players_two.append(Player.read(list(game.items())[0][1][0][1][0]))
        cls.MENU_VIEW.round_report(
            round_dict, round_name, games, players_one, players_two
        )

    @classmethod
    def round_or_classment(cls, tournament):
        """
        This method ask the user if he wants to modify the players classment.
        Args:
            tournament: the Tournament instance

        Returns:
            void.
        """
        choice = cls.MENU_VIEW.round_or_classment()
        if choice == 1:
            pass
        elif choice == 2:
            for player in tournament.players:
                m_o_n = cls.MENU_VIEW.show_player_classment(player)
                if m_o_n == 1:
                    player.update(player.id, "classment", cls.MENU_VIEW.classment())
                else:
                    pass
