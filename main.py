from models import Player
from views import MenuView, MenuViewPlayer

if __name__ == "__main__":
    menu_view = MenuView
    user_choice = menu_view.display_main()
    if user_choice == 1:
        player_menu_choice = menu_view.display_player()
        if player_menu_choice == 1:
            player_menu = MenuViewPlayer()
            user_info = player_menu.add_player()
            user = Player(user_info)
            print(f"Bonjour, {user.name} {user.lastname}.\n"
                  f"Tu es ne le {user.birthday}."
                  )
