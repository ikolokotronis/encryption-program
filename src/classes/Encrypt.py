from abc import ABC


class Encrypt(ABC):
    def __init__(self, text, mode):
        self.text = text
        self.mode = mode
        self.run(mode)

    def run(self, mode):
        options = {'1': self.rot13, '2': self.rot47}
        options.get(mode)()

    def rot13(self):
        print('selected rot13! text:', self.text)

    def rot47(self):
        print('selected rot47! text:', self.text)