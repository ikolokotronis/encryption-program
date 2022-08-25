from src.factories.menu_options import MENU_OPTIONS


class Menu:
    def __init__(self):
        self.options = MENU_OPTIONS.copy()

    def print_menu(self):
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    def get_choice(self):
        choice = input("Enter your choice: ")
        print("\n")
        return choice

    def get_file(self):
        input_file = input("Enter file name: ")
        print("\n")
        return input_file
