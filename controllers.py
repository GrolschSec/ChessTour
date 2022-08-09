import sys

from models import Player, Tournament, Database
from views import MenuView


class MenuController:
    MENU_VIEW = MenuView()

    @classmethod
    def run(cls):
        while True:
            menu_choice = cls.MENU_VIEW.display_main()
            if menu_choice == 1:
                cls.run_player()
            elif menu_choice == 2:
                cls.run_tournament()
            elif menu_choice == 3:
                cls.quit_program()
            else:
                cls.MENU_VIEW.check_max_input(3)

    @classmethod
    def run_player(cls):
        while True:
            menu_choice = cls.MENU_VIEW.display_player()
            if menu_choice == 1:
                Player(cls.MENU_VIEW.add_player()).create()
            elif menu_choice == 2:
                cls.show_players()
                player_id = cls.check_id(cls.MENU_VIEW.ID_MODIFY)
                player_info = Player.read(player_id)
                player_update = cls.MENU_VIEW.modify_player(
                    player_id, player_info.get_serialized_player()
                )
                Player.update(
                    player_update[0], player_update[1], player_update[2]
                )
            elif menu_choice == 3:
                cls.show_players()
                id_player = cls.check_id(cls.MENU_VIEW.ID_REMOVE)
                Player.delete(id_player)
            elif menu_choice == 4:
                cls.show_players()
            elif menu_choice == 5:
                break
            else:
                cls.MENU_VIEW.check_max_input(5)

    @classmethod
    def run_tournament(cls):
        while True:
            menu_choice = cls.MENU_VIEW.tournament_view()
            if menu_choice == 1:
                i = 0
                tournament = Tournament(cls.get_tournament_info())
                cls.tournament(tournament, i)
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                break
            else:
                cls.MENU_VIEW.check_max_input(3)

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
                identifier = cls.MENU_VIEW.get_id(message)
                if not Database.user_id_exist(identifier):
                    raise ValueError
            except ValueError:
                MenuView.get_id_error()
                continue
            break
        return identifier

    @classmethod
    def show_players(cls):
        """
        This function show the list of all players registered in the database.
        """
        cls.MENU_VIEW.show_all_player(Player.read_all())

    @classmethod
    def quit_program(cls):
        """
        This function exit the program properly.
        """
        cls.MENU_VIEW.quit_program()
        sys.exit(0)

    @classmethod
    def get_tournament_info(cls):
        """
        This function get the info of the tournament
        (Name, place, number of rounds, type of games, and the players instances).
        Returns:
            tour_info: a dictionary that contains all the tournament information.
        """
        tour_info = cls.MENU_VIEW.get_tournament_info()
        id_list = []
        cls.show_players()
        for i in range(1, 9):
            identifier = cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)
            id_list.append(identifier)
        tour_info.update({"player_ids": id_list})
        return tour_info

    @classmethod
    def tournament(cls, tournament, i):
        if cls.MENU_VIEW.save_tournament_to_db():
            tournament.create()
        else:
            return
        if cls.MENU_VIEW.begin_tournament():
            while i < tournament.round_number:
                round_r = tournament.sort_round(i)
                cls.MENU_VIEW.show_games(round_r.games)
                if cls.MENU_VIEW.save_tournament_to_db():
                    round_res = cls.MENU_VIEW.game_win(round_r.games)
                    tournament.save_round(round_r, round_res, i)
                else:
                    return
                i += 1
            tournament.end_tournament()
