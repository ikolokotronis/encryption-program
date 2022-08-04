from Encrypt import Encrypt


class Menu:
    def __init__(self):
        self.menu = {
            "1": Encrypt,
            "2": "Decrypt",
            "3": "Exit"
        }

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()
            text = self.get_input_text()
            mode = self.get_mode()
            self.factory(choice, text, mode)

    def print_menu(self):
        print("\n")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        print("\n")

    def get_choice(self):
        choice = input("Enter your choice: ")
        return choice

    def get_mode(self):
        mode = input("Enter mode: ").lower()
        return mode

    def get_input_text(self):
        input_text = input("Enter your text: ")
        return input_text

    def get_file(self):
        input_file = input("Enter file name: ")
        return input_file

    def factory(self, choice, text, mode):
        return self.menu.get(choice)(text, mode)  # returns object or exits


if __name__ == "__main__":
    Menu().run()