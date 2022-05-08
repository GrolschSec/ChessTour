from models import Player
from views import MenuView, MenuViewPlayer

if __name__ == "__main__":
    menu_view = MenuView
    user_choice = menu_view.display_main()
    if user_choice == 1:
        player_menu_choice = menu_view.display_player()
        player_menu = MenuViewPlayer()
        if player_menu_choice == 1:
            user_info = player_menu.add_player()
            user = Player(user_info)
            user.create_player()
        elif player_menu_choice == 2:
            new_player_info = player_menu.modify_player()
            user = Player.update_player(
                new_player_info[0], new_player_info[1], new_player_info[2]
            )
        elif player_menu_choice == 3:
            user_to_delete = player_menu.remove_player()
            user = Player.delete_player(user_to_delete)
        elif player_menu_choice == 4:
            players = Player.read_all_players()
            show_users = player_menu.show_all_player(players)
