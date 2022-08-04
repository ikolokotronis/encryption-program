from abc import ABC
import codecs


class Encrypt(ABC):
    def __init__(self, buffer, mode):
        self.buffer = buffer
        self.mode = mode
        self.run(mode)

    def run(self, mode):
        options = {'1': self.rot13, '2': self.rot47}
        options.get(mode)()

    def rot13(self):
        print("\n")
        print('Selected ROT13!')
        print("\n")
        print('Currently encrypting', self.buffer.get_buffer())
        print("\n")
        encrypted_text = codecs.encode(self.buffer.get_buffer(), 'rot_13')
        self.buffer.set_buffer(encrypted_text)
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)

    def rot47(self):
        print("\n")
        print('Selected ROT47!')
        print("\n")
        print('Currently encrypting', self.buffer.get_buffer())
        print("\n")
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