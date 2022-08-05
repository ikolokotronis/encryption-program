from Encrypt import Encrypt
from Buffer import Buffer


class Menu:
    def __init__(self):
        self.buffer = Buffer('')
        self.menu = {
            "1": Encrypt,
            "2": "Decrypt",
            "3": "Peek buffer",
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
                self.__save_buffer_to_file()
                continue
            if choice == "3":
                self.__peek_buffer()
                continue
            self.__run_factory(choice)

    def __save_to_file(self, file, text):
        with open(file, 'w') as f:
            f.write(text)
        print("Saved to file successfully")
        print("Buffer cleared")
        return text

    def __peek_buffer(self):
        print(f'Current buffer: {self.buffer.get_buffer()}')
        print("\n")
        return self.buffer.get_buffer()

    def __run_factory(self, choice):
        text = self.get_input_text()
        self.buffer.set_buffer(text)
        buffer = self.buffer
        mode = self.get_mode()
        return self.factory(choice, buffer, mode)

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
        return input_text

    def get_file(self):
        input_file = input("Enter file name: ")
        print("\n")
        return input_file

    def factory(self, choice, buffer, mode):
        return self.menu.get(choice)(buffer, mode)  # returns object

    def __save_buffer_to_file(self):
        file = self.get_file()
        text = self.buffer.get_buffer()
        with open(file, 'w') as f:
            f.write(text)
        self.buffer.set_buffer('')
        print("Saved to file successfully")
        print("Buffer cleared")
        return text


if __name__ == "__main__":
    Menu().run()