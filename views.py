from datetime import date


class MenuView:
    ID_MODIFY = "Enter the id of the player you want to modify: "
    ID_REMOVE = "Enter the ID of the player you want to remove: "
    SELECT_PLAYER = "Select a Player: "

    def display_main(self):
        """
        This function print the main menu of the application.
        Returns:
            an int, the choice of submenu to go.
        """
        print(
            "############## WELCOME TO CHESSTOUR ##############\n"
            "(1) - Player Menu.\n"
            "(2) - Tournament.\n"
            "(3) - Quit the program.\n"
        )
        return self.check_int("Choose an option: ")

    def display_player(self):
        """
        This function print the player menu.
        Returns:
            an int, the action to execute.
        """
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
        """
        This function just print the message when exiting the app.
        Returns:
            void.
        """
        print("Quitting the program...")

    @staticmethod
    def max_input(num_max):
        """
        This function print an error message if the input number is too low or too high.
        Args:
            num_max: The input number max.

        Returns:
            void.
        """
        print(f"Input must be a number between 1 and {num_max}.\n")

    @staticmethod
    def check_str(message):
        """
        This function check an input a return it if only alpha characters are in it.
        Args:
            message: The message to print.

        Returns:
            var: the string entered.
        """
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
        """
        This function if an input only contain an int.
        Args:
            message: The message to show for the input.

        Returns:
            var: an int.
        """
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
        """
        This function check the input for the birthday with a lot of parameters.
        Args:
            message: The message to show for the input.

        Returns:
            var: the birthday.
        """
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
        """
        Get the id:
        Args:
            message: Message to show

        Returns:
            int: the identity.

        """
        return self.check_int(message)

    @staticmethod
    def id_error(mode):
        """
        This function print an error message.
        Args:
            mode: 1 or 2 for the type of error.

        Returns:
            void.
        """
        if mode == 1:
            print("Identifier doesn't exist !")
        elif mode == 2:
            print("User already selected !")

    def name(self):
        """
        This function ask for the name of a player.
        Returns:
            a string that contain the name of the player.
        """
        return self.check_str("Enter the name of the player: ")

    def lastname(self):
        """
        This function ask for the lastname of a player.
        Returns:
            a string that contain the lastname of the player.
        """
        return self.check_str("Enter the last name of the player: ")

    def birthday(self):
        """
        This function ask for the birthday of a player.
        Returns:
            a string that contains the birthday (dd/mm/yyyy).
        """
        return self.check_birthday(
            "Enter the birthday of the player: (format: dd/mm/yyyy): "
        )

    def sex(self):
        """
        This function ask for the sex of a player.
        Returns:
            a char "M" for man or "W" for women.
        """
        return self.sex_input("Enter the sex of the player ('M' or 'W'): ")

    def classment(self):
        """
        This function ask for the classment of a Player (a positive number).
        Returns:
            the classment of the player (int).
        """
        classment = 0
        while True:
            try:
                classment = self.check_int("Enter the classment of the player: ")
                if classment < 1:
                    raise ValueError
            except ValueError:
                print("Classment of the player must be greater than 0.")
                continue
            break
        return classment

    def choose_an_option(self, maxint):
        choice = 0
        while True:
            try:
                choice = self.check_int("Choose an option:\t")
                if not 0 < choice < (maxint + 1):
                    raise ValueError
            except ValueError:
                self.max_input(maxint)
                continue
            break
        return choice

    @staticmethod
    def description(message):
        """
        This function ask for the description of a tournament.
        Args:
            message: The message to show while asking

        Returns:
            var: the string that contain the description.
        """
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
        """
        This function ask for the number of round of a tournament.
        Returns:
            num: an int >= 4
        """
        while True:
            num = input("Enter the number of round: (default: 4) ")
            if not num:
                return 4
            elif num.isnumeric() and int(num) >= 4:
                return num
            else:
                print("Input must be a number (minimum: 4) !")

    def time_control(self):
        """
        This function ask for the can of time control for the games.
        Returns:
            a string that contain the type of game (Blitz, Bullet, Coup rapide).
        """
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
        """
        This function check the input for the sex.
        Args:
            message: the message to show

        Returns:
            the string containing the sex.
        """
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
        """
        This function ask for which parameter of a user to modify.
        Args:
            user_info: the dictionary with all the user information.

        Returns:
            param: the parameter to modify.
        """
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
        """
        This function get all the parameter to create a player.
        Returns:
            a dict that contains all the info about the player.
        """
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
        """
        This function get the new value of a parameter to modify for a player.
        Args:
            identifier: the id of the player to modify
            user_info: The player information we got from database.

        Returns:
            a list: [the id of the player to modify, the parameter to modify, the new value of the parameter].

        """
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
        """
        This function print all the users.
        Args:
            all_player: a list of dictionary that correspond to all the players saved into db.

        Returns:
            void
        """
        maximum = len(all_player[1])
        print("(ID) - NAME - LASTNAME\n")
        for i in range(0, maximum):
            print(
                f"({all_player[1][i]}) - {all_player[0][i]['name']} {all_player[0][i]['lastname']}"
            )
            i += 1
        print("\n")

    @staticmethod
    def show_players_tournament(tournament):
        for player in tournament.players:
            print(
                f"[{player.id}] Name: {player.name} - Lastname: {player.lastname} - Classment: {player.classment}"
            )

    def display_tournament(self):
        """
        This function print the tournament menu and ask for which action to execute.
        Returns:
            an int that mean the action to execute.
        """
        print(
            "############## TOURNAMENT MENU ##############\n"
            "(1) - New tournament.\n"
            "(2) - Continue a tournament.\n"
            "(3) - Report Menu.\n"
            "(4) - Back to main menu.\n"
        )
        return self.check_int("Choose an option: ")

    def tournament_info(self):
        """
        This function get all the information to make a tournament.
        Returns:
            info: a dictionary containing all the info of a tournament.
        """
        info = {
            "name": self.check_str("Name: "),
            "location": self.check_str("Location: "),
            "round_number": self.round_number(),
            "time_control": self.time_control(),
            "description": self.description("Description: "),
            "begin_date_time": None,
            "end_date_time": None,
        }
        return info

    @staticmethod
    def show_games(games):
        """
        This function show the game of a round with also who is playing black or white.
        Args:
            games: the list of Game instance.

        Returns:
            void.
        """
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
        """
        This function ask the games result for a round.
        Args:
            games: the list of the games of the round.

        Returns:
            a list of int that correspond to the winner of each game.
        """
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
        """
        This function ask a question then you have to answer yes or no.
        Args:
            message: the message to print

        Returns:
            bool: True if yes, False if no.
        """
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
        """
        This function ask if you want to begin the tournament.
        Returns:
            bool: True if yes, False if no.
        """
        return self.yes_or_no("Do you want to begin the tournament ? (Y/n):\t")

    def save_to_db(self):
        """
        This function asl if you want to save a tournament to database.
        Returns:
            bool: True if yes, False if no.
        """
        return self.yes_or_no("Save to Database ? (Y/n):\t")

    def play_the_round(self):
        """
        This function ask the user if he wants to play the round.
        Returns:
            bool: True if yes, False if no.
        """
        return self.yes_or_no("Play the round ? (Y/n):\t")

    @staticmethod
    def end_tournament():
        """
        This function print a message at the end of the tournament.
        Returns:
            void.
        """
        print("End of the tournament !")

    def delete_player(self):
        """
        This function ask the user if he wants to delete the player he selected before
        Returns:
            bool: True if yes, False if no.
        """
        return self.yes_or_no("Are you sure you want to delete this player ? (Y/n):\t")

    def continue_tournament(self):
        """
        This function ask a user if he wants to continue the tournament.
        Returns:
            bool: True if yes, False if no
        """
        return self.yes_or_no("Do you want to continue the tournament ? (Y/n):\t")

    def tournament_msg(self, i):
        """
        This function is used when continuing a tournament,
         it will select the good message to show depending on the index of the tournament.

        Args:
            i: the index of the tournament.

        Returns:
            Depending on the index it will call the view begin_tournament or continue_tournament.
        """
        if i == 0:
            return self.begin_tournament()
        else:
            return self.continue_tournament()

    @staticmethod
    def player_deleted():
        """
        This function print a message when a user has been deleted.
        Returns:
            void.
        """
        print("Player deleted !")

    @staticmethod
    def nothing_to_continue():
        """
        This function print a message if there is no tournament available to continue.
        Returns:
            void.
        """
        print("There is no tournament available in database.")

    def display_reports(self):
        """
        This function print the report menu and ask for which submenu to go.
        Returns:
            an int the choice of submenu.
        """
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
        """
        This function show the user_report menu.
        Returns:
            the choice a value between 1 and 3.
        """
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
        """
        This function display the unfinished tournaments.
        Args:
            tournaments: The list of the instances of tournament.

        Returns:
            id: the id of the tournament you want to show the rounds
        """
        for tournament in tournaments:
            print(
                f"\t\t\t[{tournament.id}] - Name: {tournament.name} - Location: {tournament.location}\n"
                f"Time Control: {tournament.gamestype} - Begin Date Time: {tournament.begin_date_time}\n\n"
            )
        return self.check_int(
            "Enter the id of the tournament you want to continue, or (99) to go back:\t"
        )

    def show_f_tournaments(self, tournaments):
        """
        This function display the finished tournaments.
        Args:
            tournaments: The list of the instances of tournament.

        Returns:
            id: the id of the tournament you want to show the rounds
        """
        for tournament in tournaments:
            print(
                f"\t\t\t[{tournament.id}] - Name: {tournament.name} - Location: {tournament.location}\n"
                f"Time Control: {tournament.gamestype} - Begin Date Time: {tournament.begin_date_time}\n"
                f"\t\t\tEnd Date Time: {tournament.end_date_time}\n\n"
            )
        return self.check_int("Enter the id of a tournament or (99) to go back:\t")

    def tournament_report(self, tournament, tournament_rounds):
        """
        This function print the report of the tournament.
        Args:
            tournament: the instance of the tournament.
            tournament_rounds: the dictionary containing the rounds.

        Returns:
            void.
        """
        print(
            f"Name: {tournament.name} - Location: {tournament.location} - Time Control: {tournament.gamestype}\n"
            f"Round Numbers: {tournament.round_number} - Begin Date Time: {tournament.begin_date_time}\n"
            f"\t\t\tEnd Date Time: {tournament.end_date_time}\n"
            f"(1) - See players of the tournament.\n"
            f"(2) - See the rounds of the tournament.\n"
        )
        choice = self.choose_an_option(2)
        if choice == 1:
            pass
        elif choice == 2:
            for keys in tournament_rounds.keys():
                print(f"- {keys}: [{tournament_rounds[keys]}]")
        return choice

    def round_id(self):
        """
        This function ask for the round the user wants to see details or 99 to return.
        Returns:
            an int: the round id or 99.
        """
        return self.check_int(
            "Enter the id of the round you want to see report or (99) to return:\t"
        )

    @staticmethod
    def round_report(round_dict, round_name, games, player_one, player_two):
        """
        This function show the round info and the games.
        Args:
            round_dict: the dict containing the round info
            round_name: the name of the round.
            games: the list of the games.
            player_one: This list of players that where player_one.
            player_two: This list of players that where player_two.

        Returns:
            void.
        """
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

    def round_or_classment(self):
        """
        This method ask the user if he wants to modify the classment or go to next round.
        Returns:
            an int.
        """
        print("(1) - Next round.\n" "(2) - Modify players classment.\n")
        return self.choose_an_option(2)

    def show_player_classment(self, player):
        """
        This method print the player name, lastname and classment and ask if we want to modify it.
        Args:
            player: the player instance.

        Returns:
            an int.
        """
        print(
            f"Name: {player.name} - Lastname: {player.lastname} - Classment: {player.classment}\n"
            "(1) - Modify the classment of the player\n"
            "(2) - Continue\n"
        )
        return self.choose_an_option(2)

    def select_players_view(self):
        """
        This method print a choice to shwo the player in the report menu.
        Returns:
            an int, the option.
        """
        print(
            "(1) -  Show players by alphabet order.\n"
            "(2) - Show players by classment.\n"
        )
        return self.choose_an_option(2)
