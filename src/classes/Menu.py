class Menu:
    def __init__(self):
        self.options = ['Encrypt', 'Decrypt',
                        'Peek buffer', 'Save to file', 'Exit']

    def print_menu(self):
        for index, option in enumerate(self.options):
            print(f'{index+1}. {option}')

    # TODO get_choice dziedziczenie

    def get_choice(self):
        choice = input("Enter your choice: ")
        print("\n")
        return choice

    def get_file(self):
        input_file = input("Enter file name: ")
        print("\n")
        return input_file

