import codecs

from src.utils.Rot import Rot


class ROT13(Rot):
    def encrypt(self, plain_text):
        print("\n")
        print("Selected ROT13!")
        print("Text to be encrypted:", plain_text)
        encrypted_text = codecs.encode(plain_text, "rot_13")
        print("Encrypted successfully!")
        print("Encrypted text:", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        print("\n")
        print("Selected ROT13!")
        print("Text to be decrypted:", encrypted_text)
        decrypted_text = codecs.decode(encrypted_text, "rot_13")
        print("Decrypted successfully!")
        print("Decrypted text:", decrypted_text)
        return decrypted_text
