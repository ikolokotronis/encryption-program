from src.classes.Buffer import Buffer
from src.classes.Menu import Menu
from src.classes.Messenger import Messenger
from src.classes.RotMenu import RotMenu
from src.exceptions.InvalidChoice import InvalidChoice
from src.factories.RotFactory import RotFactory


class Manager:
    '''

    '''
    def __init__(self):
        self.is_running = True
        self.buffer = Buffer('')
        self.menu = Menu()
        self.rot_menu = RotMenu()
        self.menu_options = {
            "1": self.__encrypt,
            "2": self.__decrypt,
            "3": self.__peek_buffer,
            "4": self.__save_buffer_to_file,
            "5": self.__exit
        }

    def __exit(self):
        self.is_running = False

    def run(self):
        while self.is_running is True:
            self.menu.print_menu()
            choice = self.menu.get_choice()
            self.__execute(choice)

    def __execute(self, choice):
        try:
            self.menu_options.get(choice, Messenger.no_such_option)()
        except InvalidChoice:
            print('No such option!')

    def __encrypt(self):
        self.rot_menu.show_options()
        rot_choice = self.rot_menu.get_choice()
        rot = ''
        try:
            rot = RotFactory.produce(rot_choice)
        except InvalidChoice:
            print('No such option!')
            return
        plain_text = self.rot_menu.get_plain_text()
        encrypted_text = rot.encrypt(plain_text)
        self.buffer.set_buffer(encrypted_text)

    def __decrypt(self):
        self.rot_menu.show_options()
        rot_choice = self.rot_menu.get_choice()
        rot = RotFactory.produce(rot_choice)
        file_name = self.get_file_name()
        encrypted_text = ''
        with open('content/'+file_name, 'r', encoding='utf-8') as f:
            encrypted_text = f.read()
        decrypted_text = rot.decrypt(encrypted_text)
        self.buffer.set_buffer(decrypted_text)

    def __peek_buffer(self):
        print(f'Current buffer: {self.buffer.get_buffer()}')
        print("\n")
        return self.buffer.get_buffer()

    #  TODO: wydziel filehandler jako klase
    def __save_buffer_to_file(self):
        file_name = self.get_file_name()
        text = self.buffer.get_buffer()
        with open('content/'+file_name, 'w') as f:
            f.write(text)
        self.buffer.set_buffer('')
        print("Saved to file successfully")
        print("Buffer cleared")
        return text

    def get_file_name(self):
        file_name = input('Enter file name: ')
        return file_name
