from datetime import date


class MenuView:
    @classmethod
    def display_main(cls):
        print(
            "############## WELCOME TO CHESSTOUR ##############\n"
            "(1) - Player Menu.\n"
            "(2) - Tournament.\n"
            "(3) - Quit the program.\n"
        )
        return cls.check_int_input("Choose an option: ")

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
        return cls.check_int_input("Choose an option: ")

    @staticmethod
    def check_str_input(message):
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
    def check_int_input(message):
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
    def check_birthday_input(message):
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
    def check_sex_input(cls, message):
        while True:
            try:
                var = cls.check_str_input(message).upper()
                if var == "M" or var == "W":
                    return var
                else:
                    raise ValueError
            except ValueError:
                print("Input must be: 'M' or 'W'.\n")
                continue

    @classmethod
    def check_param_input(cls):
        param_choice = ""
        while True:
            try:
                param_choice = cls.check_int_input(
                    "Which parameter would you like to modify: \n"
                    "1: Name.\n"
                    "2: Lastname.\n"
                    "3: Birthday.\n"
                    "4: Sex.\n"
                    "5: Classment.\n"
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
    def check_y_or_n(cls, message):
        inp = ""
        while True:
            try:
                inp = cls.check_str_input(message)
                if inp.upper() == "Y" or inp.upper() == "N":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Input must be 'Y' or 'N'. ")
                continue
        return inp.upper()

    @classmethod
    def get_name(cls):
        return cls.check_str_input("Enter the name of the player: ")

    @classmethod
    def get_lastname(cls):
        return cls.check_str_input("Enter the last name of the player: ")

    @classmethod
    def get_birthday(cls):
        return cls.check_birthday_input(
            "Enter the birthday of the player: (format: dd/mm/yyyy): "
        )

    @classmethod
    def get_sex(cls):
        return cls.check_sex_input("Enter the sex of the player ('M' or 'W'): ")

    @classmethod
    def get_classment(cls):
        return cls.check_int_input("Enter the classment of the player: ")

    @classmethod
    def add_player(cls):
        player_info = {
            "name": cls.get_name(),
            "lastname": cls.get_lastname(),
            "birthday": cls.get_birthday(),
            "sex": cls.get_sex(),
            "classment": cls.get_classment(),
        }
        print("Done ! Player created.\n")
        return player_info

    @classmethod
    def remove_player(cls):
        result = cls.check_int_input("Enter the ID of the player you want to remove: ")
        confirm = cls.check_y_or_n("Are you sure you want to delete the user (Y/n): ")
        if confirm != "Y":
            return
        print("Player deleted !\n")
        return result

    @classmethod
    def modify_player(cls):
        new_value = ""
        identifier = cls.check_int_input(
            "Enter the ID of the player you want to modify: "
        )
        param = cls.check_param_input()
        if param == "name":
            new_value = cls.get_name()
        elif param == "lastname":
            new_value = cls.get_lastname()
        elif param == "birthday":
            new_value = cls.get_birthday()
        elif param == "sex":
            new_value = cls.get_sex()
        elif param == "classment":
            new_value = cls.get_classment()
        print("Player modified !")
        return [identifier, param, new_value]

    @classmethod
    def show_all_player(cls, all_player):
        maximum = len(all_player)
        for i in range(0, maximum):
            print(f"{all_player[i]['name']} {all_player[i]['lastname']}")
            i += 1
