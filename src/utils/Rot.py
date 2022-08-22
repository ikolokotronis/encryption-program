from abc import ABC, abstractmethod


class Rot(ABC):

    @abstractmethod
    def encrypt(self, plain_text):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, encrypted_text):
        raise NotImplementedError
