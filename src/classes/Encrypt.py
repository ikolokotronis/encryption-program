from abc import ABC


class Encrypt(ABC):
    def __init__(self, buffer, mode):
        self.buffer = buffer
        self.mode = mode
        self.run(mode)

    def run(self, mode):
        options = {'1': self.rot13, '2': self.rot47}
        options.get(mode)()

    def rot13(self):
        print('Selected ROT13! Current text:', self.buffer.get_buffer())

    def rot47(self):
        print('Selected ROT47! Current text:', self.buffer.get_buffer())