from datetime import date, datetime


class MenuView:
    ID_MODIFY = "Enter the id of the player you want to modify: "
    ID_REMOVE = "Enter the ID of the player you want to remove: "
    SELECT_PLAYER = "Select a Player: "

    def display_main(self):
        print(
            "############## WELCOME TO CHESSTOUR ##############\n"
            "(1) - Player Menu.\n"
            "(2) - Tournament.\n"
            "(3) - Quit the program.\n"
        )
        return self.check_int("Choose an option: ")

    def display_player(self):
        print(
            "################## PLAYER MENU ###################\n"
            "(1) - Add a player.\n"
            "(2) - Modify a player.\n"
            "(3) - Remove a player.\n"
            "(4) - Show all players.\n"
            "(5) - Back to main menu.\n"
        )
        return self.check_int("Choose an option: ")

    @staticmethod
    def quit_program():
        print("Quitting the program...")

    @staticmethod
    def max_input(num_max):
        print(f"Input must be a number between 1 and {num_max}.\n")

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

    def id(self, message):
        return self.check_int(message)

    @staticmethod
    def id_error(mode):
        if mode == 1:
            print("Identifier doesn't exist !")
        elif mode == 2:
            print("User already selected !")

    def name(self):
        return self.check_str("Enter the name of the player: ")

    def lastname(self):
        return self.check_str("Enter the last name of the player: ")

    def birthday(self):
        return self.check_birthday(
            "Enter the birthday of the player: (format: dd/mm/yyyy): "
        )

    def sex(self):
        return self.sex_input("Enter the sex of the player ('M' or 'W'): ")

    def classment(self):
        return self.check_int("Enter the classment of the player: ")

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

    def time_control(self):
        while True:
            time = self.check_int(
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
                self.max_input(3)

    def sex_input(self, message):
        while True:
            try:
                var = self.check_str(message).upper()
                if var == "M" or var == "W":
                    return var
                else:
                    raise ValueError
            except ValueError:
                print("Input must be: 'M' or 'W'.\n")
                continue

    def param_input(self, user_info):
        param_choice = ""
        while True:
            try:
                param_choice = self.check_int(
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

    def add_player(self):
        player_info = {
            "name": self.name(),
            "lastname": self.lastname(),
            "birthday": self.birthday(),
            "sex": self.sex(),
            "classment": self.classment(),
        }
        print("Done ! Player created.\n")
        return player_info

    def modify_player(self, identifier, user_info):
        new_value = ""
        param = self.param_input(user_info)
        if param == "name":
            new_value = self.name()
        elif param == "lastname":
            new_value = self.lastname()
        elif param == "birthday":
            new_value = self.birthday()
        elif param == "sex":
            new_value = self.sex()
        elif param == "classment":
            new_value = self.classment()
        print("Player modified !")
        return [identifier, param, new_value]

    @staticmethod
    def show_all_player(all_player):
        maximum = len(all_player[1])
        print("(ID) - NAME - LASTNAME\n")
        for i in range(0, maximum):
            print(
                f"({all_player[1][i]}) - {all_player[0][i]['name']} {all_player[0][i]['lastname']}"
            )
            i += 1
        print("\n")

    def display_tournament(self):
        print(
            "############## TOURNAMENT MENU ##############\n"
            "(1) - New tournament.\n"
            "(2) - Continue a tournament.\n"
            "(3) - Generate report of a tournament.\n"
            "(4) - Back to main menu.\n"
        )
        return self.check_int("Choose an option: ")

    def tournament_info(self):
        info = {
            "name": self.check_str("Name: "),
            "location": self.check_str("Location: "),
            "round_number": self.round_number(),
            "time_control": self.time_control(),
            "description": self.description("Description: "),
            "begin_date_time": f"{datetime.now}",
            "end_date_time": None,
        }
        return info

    @staticmethod
    def show_games(games):
        i = 0
        print("Game ID  -   Player One      -       Player Two")
        for game in games:
            if game.is_black == 1:
                player_one_color = "Black"
                player_two_color = "White"
            else:
                player_one_color = "White"
                player_two_color = "Black"
            print(
                f"{i}"
                f"        -   "
                f"{game.player_one.name} {game.player_one.lastname} ({player_one_color})"
                f"  -   "
                f"{game.player_two.name} {game.player_two.lastname} ({player_two_color})"
            )
            i += 1

    def game_win(self, games):
        results = []
        for game in games:
            results.append(
                self.check_int(
                    f"Select the winner of the game:\n"
                    f"(1) - {game.player_one.name} {game.player_one.lastname}\n"
                    f"(2) - {game.player_two.name} {game.player_two.lastname}\n"
                    f"(3) - NULL\n"
                    f"Enter 1,2 or 3: "
                )
            )
        return results

    def yes_or_no(self, message):
        choice = str
        while True:
            try:
                choice = self.check_str(message)
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

    def begin_tournament(self):
        return self.yes_or_no("Do you want to begin the tournament ? (Y/n):\t")

    def save_to_db(self):
        return self.yes_or_no("Save to Database ? (Y/n):\t")

    def play_the_round(self):
        return self.yes_or_no("Play the round ? (Y/n):\t")

    @staticmethod
    def end_tournament():
        print("End of the tournament !")

    def delete_player(self):
        return self.yes_or_no("Are you sure you want to delete this player ? (Y/n):\t")

    def continue_tournament(self):
        return self.yes_or_no("Do you want to continue the tournament ? (Y/n):\t")

    def tournament_msg(self, i):
        if i == 0:
            return self.begin_tournament()
        else:
            return self.continue_tournament()

    @staticmethod
    def player_deleted():
        print("Player deleted !")

    @staticmethod
    def nothing_to_continue():
        print("There is no tournament available in database.")

    def display_reports(self):
        choice = ""
        while True:
            try:
                choice = self.check_int(
                    "(1) - List all users.\n"
                    "(2) - List all tournaments.\n"
                    "(3) - Return\n\n"
                    "Choose an option:\t"
                )
                if 1 > choice > 3:
                    raise ValueError
            except ValueError:
                self.max_input(3)
                continue
            break
        return choice

    def users_report(self):
        choice = ""
        while True:
            try:
                choice = self.check_int(
                    "(1) - List users by alphabet order.\n"
                    "(2) - List users by classment.\n"
                    "(3) - Return\n\n"
                    "Choose an option:\t"
                )
                if 1 > choice > 3:
                    raise ValueError
            except ValueError:
                self.max_input(3)
                continue
            break
        return choice

    def show_u_tournaments(self, tournaments):
        for tournament in tournaments:
            print(
                f"\t\t\t[{tournament.id}] - Name: {tournament.name} - Location: {tournament.location}\n"
                f"Time Control: {tournament.gamestype} - Begin Date Time: {tournament.begin_date_time}\n\n"
            )
        return self.check_int(
            "Enter the id of the tournament you want to continue, or (99) to go back:\t"
        )

    def show_f_tournaments(self, tournaments):
        for tournament in tournaments:
            print(
                f"\t\t\t[{tournament.id}] - Name: {tournament.name} - Location: {tournament.location}\n"
                f"Time Control: {tournament.gamestype} - Begin Date Time: {tournament.begin_date_time}\n"
                f"\t\t\tEnd Date Time: {tournament.end_date_time}\n\n"
            )
        return self.check_int("Enter the id of a tournament or (99) to go back:\t")

    @staticmethod
    def tournament_report(tournament, tournament_rounds):
        print(
            f"Name: {tournament.name} - Location: {tournament.location} - Time Control: {tournament.gamestype}\n"
            f"Round Numbers: {tournament.round_number} - Begin Date Time: {tournament.begin_date_time}\n"
            f"\t\t\tEnd Date Time: {tournament.end_date_time}\n"
            f"Players:"
        )
        for player in tournament.players:
            print(f"- {player.name} {player.lastname}")
        print("\nRounds:")
        for key in tournament_rounds:
            print(f"- {key}: [{tournament_rounds[f'{key}']}]")
        print("\n")

    def round_id(self):
        return self.check_int(
            "Enter the id of the round you want to see report or (99) to return:\t"
        )

    @staticmethod
    def round_report(round_dict, round_name, games, player_one, player_two):
        print(
            f"[{round_name}]:\n"
            f"- Begin Date Time: {round_dict['begin_date_time']}\n"
            f"- End Date Time: {round_dict['end_date_time']}\n"
            f"Games: "
        )
        i = 0
        for game in games:
            if list(game.items())[0][1][1] == 1:
                player_one_color = "Black"
                player_two_color = "White"
            else:
                player_one_color = "White"
                player_two_color = "Black"
            print(
                f"- {list(game.keys())[0]}: [{list(game.items())[0][1][0][0][1]}] {player_one[i].name} "
                f"{player_one[i].lastname} (Played {player_one_color})"
                f" - [{list(game.items())[0][1][0][1][1]}] {player_two[i].name} "
                f"{player_two[i].lastname} (Played {player_two_color})"
            )
            i += 1
