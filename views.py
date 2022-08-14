from datetime import date


class MenuView:
    ID_MODIFY = "Enter the id of the player you want to modify: "
    ID_REMOVE = "Enter the ID of the player you want to remove: "
    SELECT_PLAYER = "Select a Player: "

    @classmethod
    def display_main(cls):
        print(
            "############## WELCOME TO CHESSTOUR ##############\n"
            "(1) - Player Menu.\n"
            "(2) - Tournament.\n"
            "(3) - Quit the program.\n"
        )
        return cls.check_int("Choose an option: ")

    @classmethod
    def display_player(cls):
        print(
            "################## PLAYER MENU ###################\n"
            "(1) - Add a player.\n"
            "(2) - Modify a player.\n"
            "(3) - Remove a player.\n"
            "(4) - Show all players.\n"
            "(5) - Back to main menu.\n"
        )
        return cls.check_int("Choose an option: ")

    @staticmethod
    def quit_program():
        print("Quitting the program...")

    @staticmethod
    def max_input(num_max):
        print(f"Input must be a number between 1 and {num_max}.")

    @staticmethod
    def check_str(message):
        var = ""
        while True:
            try:
                var = input(message)
                if not var.isalpha():
                    raise ValueError
            except ValueError:
                print("Input must be a string.")
                continue
            break
        return var

    @staticmethod
    def check_int(message):
        var = ""
        while True:
            try:
                var = int(input(message))
            except ValueError:
                print("Input must be a number.")
                continue
            break
        return var

    @staticmethod
    def check_birthday(message):
        var = ""
        while True:
            try:
                var = input(message)
                day, month, year = var.split("/")
                this_year = int(date.today().strftime("%Y"))
                if (
                    not int(day)
                    or not int(month)
                    or not int(year)
                    or int(day) < 1
                    or int(day) > 31
                    or int(month) < 1
                    or int(month) > 12
                    or len(day) != 2
                    or len(month) != 2
                    or len(year) != 4
                    or int(year) < this_year - 100
                    or int(year) > this_year
                ):
                    raise ValueError
            except ValueError:
                print("Birthday must be in format: dd/mm/yyyy")
                continue
            break
        return var

    @classmethod
    def id(cls, message):
        return cls.check_int(message)

    @staticmethod
    def id_error():
        print("Identifier doesn't exist !")

    @classmethod
    def name(cls):
        return cls.check_str("Enter the name of the player: ")

    @classmethod
    def lastname(cls):
        return cls.check_str("Enter the last name of the player: ")

    @classmethod
    def birthday(cls):
        return cls.check_birthday(
            "Enter the birthday of the player: (format: dd/mm/yyyy): "
        )

    @classmethod
    def sex(cls):
        return cls.sex_input("Enter the sex of the player ('M' or 'W'): ")

    @classmethod
    def classment(cls):
        return cls.check_int("Enter the classment of the player: ")

    @staticmethod
    def description(message):
        var = ""
        while True:
            try:
                var = input(message)
                if not var.isascii():
                    raise ValueError
            except ValueError:
                print("Input must be a string.")
                continue
            break
        return var

    @staticmethod
    def round_number():
        while True:
            num = input("Enter the number of round: (default: 4) ")
            if not num:
                return 4
            elif num.isnumeric() and int(num) >= 4:
                return num
            else:
                print("Input must be a number (minimum: 4) !")

    @classmethod
    def time_control(cls):
        while True:
            time = cls.check_int(
                "Time Control: \n"
                "(1) - Blitz.\n"
                "(2) - Bullet.\n"
                "(3) - Coup rapide.\n"
                "Choose a number: "
            )
            if time == 1:
                return "Blitz"
            elif time == 2:
                return "Bullet"
            elif time == 3:
                return "Coup rapide"
            else:
                cls.max_input(3)

    @classmethod
    def sex_input(cls, message):
        while True:
            try:
                var = cls.check_str(message).upper()
                if var == "M" or var == "W":
                    return var
                else:
                    raise ValueError
            except ValueError:
                print("Input must be: 'M' or 'W'.\n")
                continue

    @classmethod
    def param_input(cls, user_info):
        param_choice = ""
        while True:
            try:
                param_choice = cls.check_int(
                    "Which parameter would you like to modify: \n"
                    f"1: Name: {user_info['name']}.\n"
                    f"2: Lastname: {user_info['lastname']}.\n"
                    f"3: Birthday: {user_info['birthday']}.\n"
                    f"4: Sex: {user_info['sex']}.\n"
                    f"5: Classment: {user_info['classment']}.\n"
                    "Choose a number: "
                )
                if param_choice < 1 or param_choice > 5:
                    raise ValueError
            except ValueError:
                print("Input must be a number between 1 and 5")
                continue
            break
        param = ""
        if param_choice == 1:
            param = "name"
        elif param_choice == 2:
            param = "lastname"
        elif param_choice == 3:
            param = "birthday"
        elif param_choice == 4:
            param = "sex"
        elif param_choice == 5:
            param = "classment"
        return param

    @classmethod
    def add_player(cls):
        player_info = {
            "name": cls.name(),
            "lastname": cls.lastname(),
            "birthday": cls.birthday(),
            "sex": cls.sex(),
            "classment": cls.classment(),
        }
        print("Done ! Player created.\n")
        return player_info

    @classmethod
    def modify_player(cls, identifier, user_info):
        new_value = ""
        param = cls.param_input(user_info)
        if param == "name":
            new_value = cls.name()
        elif param == "lastname":
            new_value = cls.lastname()
        elif param == "birthday":
            new_value = cls.birthday()
        elif param == "sex":
            new_value = cls.sex()
        elif param == "classment":
            new_value = cls.classment()
        print("Player modified !")
        return [identifier, param, new_value]

    @classmethod
    def show_all_player(cls, all_player):
        maximum = len(all_player[1])
        print("(ID) - NAME - LASTNAME\n")
        for i in range(0, maximum):
            print(
                f"({all_player[1][i]}) - {all_player[0][i]['name']} {all_player[0][i]['lastname']}"
            )
            i += 1

    @classmethod
    def tournament_menu(cls):
        print(
            "############## TOURNAMENT MENU ##############\n"
            "(1) - New tournament.\n"
            "(2) - Continue a tournament.\n"
            "(2) - Generate report of a tournament.\n"
            "(3) - Back to main menu.\n"
        )
        return cls.check_int("Choose an option: ")

    @classmethod
    def tournament_info(cls):
        info = {
            "name": cls.check_str("Name: "),
            "location": cls.check_str("Location: "),
            "round_number": cls.round_number(),
            "time_control": cls.time_control(),
            "description": cls.description("Description: "),
        }
        return info

    @staticmethod
    def show_games(games):
        i = 0
        print("Game ID  -   Player One      -       Player Two")
        for game in games:
            print(
                f"{i}"
                f"        -   "
                f"{game.player_one.name} {game.player_one.lastname}"
                f"  -   "
                f"{game.player_two.name} {game.player_two.lastname}"
            )
            i += 1

    @classmethod
    def game_win(cls, games):
        results = []
        for game in games:
            results.append(
                cls.check_int(
                    f"Select the winner of the game:\n"
                    f"(1) - {game.player_one.name} {game.player_one.lastname}\n"
                    f"(2) - {game.player_two.name} {game.player_two.lastname}\n"
                    f"(3) - NULL\n"
                    f"Enter 1,2 or 3: "
                )
            )
        return results

    @classmethod
    def yes_or_no(cls, message):
        choice = str
        while True:
            try:
                choice = cls.check_str(message)
                if choice.upper() == "Y" or choice.upper() == "N":
                    break
                else:
                    raise ValueError
            except ValueError:
                continue
        if choice.upper() == "Y":
            return True
        elif choice.upper() == "N":
            return False

    @classmethod
    def begin_tournament(cls):
        return cls.yes_or_no("Do you want to begin the tournament ? (Y/n):\t")

    @classmethod
    def save_to_db(cls):
        return cls.yes_or_no("Save to Database ? (Y/n):\t")

    @classmethod
    def play_the_round(cls):
        return cls.yes_or_no("Play the round ? (Y/n):\t")

    @staticmethod
    def end_tournament():
        print("End of the tournament !")

    @classmethod
    def delete_player(cls):
        return cls.yes_or_no("Are you sure you want to delete this player ? (Y/n):\t")

    @classmethod
    def continue_tournament(cls):
        return cls.yes_or_no("Do you want to continue the tournament ? (Y/n):\t")

    @classmethod
    def tournament_msg(cls, i):
        if i == 0:
            return cls.begin_tournament()
        else:
            return cls.continue_tournament()

    @staticmethod
    def player_deleted():
        print("Player deleted !")

    @classmethod
    def show_tournaments(cls, tournaments):
        for tournament in tournaments:
            print(
                f"\t\t\t[{tournament.id}] - Name: {tournament.name} - Location: {tournament.location}\n"
                f"Time Control: {tournament.gamestype} - Begin Date Time: {tournament.begin_date_time}\n\n"
            )
        return cls.check_int("Enter the id of the tournament you want to continue:\t")
