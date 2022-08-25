class RotMenu:
    def __init__(self):
        self.options = ["ROT13", "ROT47"]

    def show_options(self):
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    def get_choice(self):
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")
        return choice

    def get_plain_text(self):
        print("\n")
        input_text = input("Enter your text: ")
        print("\n")
        return input_text
