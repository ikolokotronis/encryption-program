from abc import ABC, abstractmethod
import codecs
from src.utils.rot47_encoder import rot47_encoder


class Rot(ABC):

    @abstractmethod
    def encrypt(self, plain_text):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, encrypted_text):
        raise NotImplementedError

    def rot13(self):
        print(self.buffer)
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
