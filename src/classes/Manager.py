from src.classes.Buffer import Buffer
from src.classes.Menu import Menu
from src.classes.RotMenu import RotMenu
from src.factories.RotFactory import RotFactory


class Manager:
    def __init__(self):
        self.buffer = Buffer('')
        self.menu = Menu()
        self.rot_menu = RotMenu()
        self.menu_options = {
            "1": self.__encrypt,
            "2": self.__decrypt,
            "3": self.__peek_buffer,
            "4": self.__save_buffer_to_file,
            "5": "Exit"
        }

    def run(self):
        self.menu.print_menu()
        choice = self.menu.get_choice()
        self.__execute(choice)

    def __execute(self, choice):
        self.menu_options.get(choice, self.__show_error)()

    def __show_error(self):
        print('No such option!')

    def __encrypt(self):
        self.rot_menu.show_options()
        rot_choice = self.rot_menu.get_choice()
        rot = RotFactory.produce(rot_choice)
        plain_text = self.rot_menu.get_plain_text()
        encrypted_text = rot.encrypt(plain_text)
        self.buffer.set_buffer(encrypted_text)

    def __decrypt(self):
        pass

    def __peek_buffer(self):
        print(f'Current buffer: {self.buffer.get_buffer()}')
        print("\n")
        return self.buffer.get_buffer()

    def __save_buffer_to_file(self):
        file = self.get_file()
        text = self.buffer.get_buffer()
        with open(file, 'w') as f:
            f.write(text)
        self.buffer.set_buffer('')
        print("Saved to file successfully")
        print("Buffer cleared")
        return text