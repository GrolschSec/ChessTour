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
                Player(cls.MENU_VIEW.add_player()).create_player()
            elif menu_choice == 2:
                cls.show_players()
                player_id = cls.check_id(cls.MENU_VIEW.ID_MODIFY)
                player_info = Player.read_player(player_id)
                player_update = cls.MENU_VIEW.modify_player(
                    player_id, player_info.get_serialized_player()
                )
                Player.update_player(
                    player_update[0], player_update[1], player_update[2]
                )
            elif menu_choice == 3:
                cls.show_players()
                id_player = cls.check_id(cls.MENU_VIEW.ID_REMOVE)
                Player.delete_player(id_player)
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
                print(cls.get_tournament_info())
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                break
            else:
                cls.MENU_VIEW.check_max_input(3)

    @classmethod
    def check_id(cls, message):
        identifier = int
        while True:
            try:
                identifier = cls.MENU_VIEW.get_id(message)
                if Database.check_id(identifier) == 1:
                    raise ValueError
            except ValueError:
                MenuView.get_id_error()
                continue
            break
        return identifier

    @classmethod
    def show_players(cls):
        cls.MENU_VIEW.show_all_player(Player.read_all_players())

    @classmethod
    def quit_program(cls):
        cls.MENU_VIEW.quit_program()
        sys.exit(0)

    @classmethod
    def get_tournament_info(cls):
        tour_info = cls.MENU_VIEW.get_tournament_info()
        cls.show_players()
        tour_info.update({"id1": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id2": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id3": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id4": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id5": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id6": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id7": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        tour_info.update({"id8": cls.check_id(cls.MENU_VIEW.SELECT_PLAYER)})
        return tour_info
