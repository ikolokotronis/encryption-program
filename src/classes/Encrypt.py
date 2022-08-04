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
        print('Selected ROT13!')
        print('Currently encrypting', self.buffer.get_buffer())
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        encrypted_text = "".join([alphabet[(alphabet.find(char) + 13) % 26] for char in self.buffer.get_buffer()])
        self.buffer.set_buffer(encrypted_text)
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)

    def rot47(self):
        print('Selected ROT47!')
        print('Currently encrypting', self.buffer.get_buffer())
        x = []
        for i in range(len(self.buffer.get_buffer())):
            j = ord(self.buffer.get_buffer()[i])
            if j >= 33 and j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(self.buffer.get_buffer()[i])
        encrypted_text = ''.join(x)
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)