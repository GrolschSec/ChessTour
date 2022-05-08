from models import Player
from views import MenuView


class Controller:
    MENU_VIEW = MenuView()

    @classmethod
    def run(cls):
        while True:
            user_choice = cls.MENU_VIEW.display_main()
            if user_choice == 1:
                cls.run_player()
            elif user_choice == 2:
                pass
            elif user_choice == 3:
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
                player_info = cls.MENU_VIEW.modify_player()
                Player.update_player(player_info[0], player_info[1], player_info[2])
            elif menu_choice == 3:
                Player.delete_player(cls.MENU_VIEW.remove_player())
            elif menu_choice == 4:
                cls.MENU_VIEW.show_all_player(Player.read_all_players())
            elif menu_choice == 5:
                break
            else:
                print("Input must be a number between 1 and 5.\n")
