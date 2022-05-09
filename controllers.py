from models import Player
from views import MenuView


class Controller:
    MENU_VIEW = MenuView()

    @classmethod
    def run(cls):
        while True:
            menu_choice = cls.MENU_VIEW.display_main()
            if menu_choice == 1:
                cls.run_player()
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                print("Quitting the program...")
                break
            else:
                print("Input must be a number between 1 and 3.")

    @classmethod
    def run_player(cls):
        while True:
            menu_choice = cls.MENU_VIEW.display_player()
            if menu_choice == 1:
                Player(cls.MENU_VIEW.add_player()).create_player()
            elif menu_choice == 2:
                cls.show_players()
                player_id = cls.MENU_VIEW.get_player_id(Player.read_all_players()[1])
                player_info = Player.read_player(player_id)
                player_update = cls.MENU_VIEW.modify_player(
                    player_id, player_info.get_serialized_player()
                )
                Player.update_player(
                    player_update[0], player_update[1], player_update[2]
                )
            elif menu_choice == 3:
                cls.show_players()
                id_player = cls.MENU_VIEW.remove_player(Player.read_all_players()[1])
                Player.delete_player(id_player)
            elif menu_choice == 4:
                cls.show_players()
            elif menu_choice == 5:
                break
            else:
                print("Input must be a number between 1 and 5.\n")

    @classmethod
    def show_players(cls):
        cls.MENU_VIEW.show_all_player(Player.read_all_players())
