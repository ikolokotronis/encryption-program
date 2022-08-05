from abc import ABC
import codecs
from ..utils.rot47_encoder import rot47_encoder


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
        encrypted_text = rot47_encoder(self.buffer.get_buffer())
        self.buffer.set_buffer(encrypted_text)
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)