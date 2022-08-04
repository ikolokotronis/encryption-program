from Encrypt import Encrypt
from Buffer import Buffer


class Menu:
    def __init__(self):
        self.buffer = Buffer('')
        self.menu = {
            "1": Encrypt,
            "2": "Decrypt",
            "3": self.buffer.get_buffer(),
            "4": "Save to file",
            "5": "Exit"
        }

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()
            if choice == "5":
                break
            if choice == "4":
                file = self.get_file()
                text = self.buffer.get_buffer()
                self.save_to_file(file, text)
                self.buffer.set_buffer('')
                continue
            if choice == "3":
                print(f'Current buffer: {self.buffer.get_buffer()}')
                print("\n")
                continue
            self.get_input_text()
            mode = self.get_mode()
            self.factory(choice, self.buffer, mode)

    def print_menu(self):
        print("\n")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Peek buffer")
        print("4. Save to file")
        print("5. Exit")
        print("\n")

    def get_choice(self):
        choice = input("Enter your choice: ")
        print("\n")
        return choice

    def get_mode(self):
        print("1. ROT13")
        print("2. ROT47")
        print("\n")
        mode = input("Enter mode: ").lower()
        print("\n")
        return mode

    def get_input_text(self):
        input_text = input("Enter your text: ")
        print("\n")
        self.buffer.set_buffer(input_text)
        return input_text

    def get_file(self):
        input_file = input("Enter file name: ")
        print("\n")
        return input_file

    def factory(self, choice, text, mode):
        return self.menu.get(choice)(text, mode)  # returns object

    def save_to_file(self, file, text):
        with open(file, 'w') as f:
            f.write(text)
        return text


if __name__ == "__main__":
    Menu().run()