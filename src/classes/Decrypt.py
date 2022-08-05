from abc import ABC


class Decrypt(ABC):
    def __init__(self, buffer, mode):
        self.buffer = buffer
        self.mode = mode
        self.run(mode)

    def run(self, mode):
        options = {'1': self.rot13, '2': self.rot47}
        options.get(mode)()

    def rot13(self):
        pass

    def rot47(self):
        pass
