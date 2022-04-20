from datetime import date


class MenuView:
    @staticmethod
    def display_main():
        print(
            "############## WELCOME TO CHESSTOUR ##############\n"
            "(1) - Player Menu\n"
            "(2) - Tournament\n"
        )
        return int(input("Choose an option: "))

    @staticmethod
    def display_player():
        print(
            "\n\n\n\n################## PLAYER MENU ###################\n"
            "(1) - Add a player.\n"
            "(2) - Remove a player.\n"
            "(3) - Modify a player.\n"
            "(4) - Show all players.\n"
            "(5) - Back to main menu.\n"
        )
        return int(input("Choose an option: "))


class MenuViewPlayer(MenuView):
    @staticmethod
    def check_str_input(message):
        var = ""
        while True:
            try:
                var = input(message)
                if not var.isalpha():
                    raise ValueError
            except ValueError:
                print("The entry must be a string.")
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
                print("The entry must be a number")
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
                if not int(day) or not int(month) or not int(year):
                    raise ValueError
                if len(day) != 2 or len(month) != 2 or len(year) != 4:
                    raise ValueError
                if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12:
                    raise ValueError
                this_year = int(date.today().strftime("%Y"))
                if int(year) < this_year - 100 or int(year) > this_year:
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
                if var == "M" or var == "W" or var == "NB":
                    return var
                else:
                    raise ValueError
            except ValueError:
                print("Input must be: 'M', 'W' or 'NB'.\n")
                continue

    @classmethod
    def add_player(cls):
        name = cls.check_str_input("Enter the name of the player: ")
        lastname = cls.check_str_input("Enter the last name of the player: ")
        birthday = cls.check_birthday_input("Enter the birthday of the player: ")
        sex = cls.check_sex_input("Enter the sex of the player ('M', 'W' or 'NB'): ")
        classment = cls.check_int_input("Enter the classment of the player: ")
        print("######################################\n"
              "########Done ! Player created.########\n"
              "######################################\n")
        player_info = {
            "name": name,
            "lastname": lastname,
            "birthday": birthday,
            "sex": sex,
            "classment": classment,
        }
        return player_info

    @classmethod
    def remove_player(cls):
        name = cls.check_str_input("Enter the name of the player you want to delete: ")
        lastname = cls.check_str_input(
            "Enter the lastname of the player you want to delete: "
        )
        print(f"Deleting the user {name} {lastname}.\n" "User deleted !")
        result = {"name": name, "lastname": lastname}
        return result
