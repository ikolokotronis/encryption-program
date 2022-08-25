import codecs

from src.utils.Rot import Rot


class ROT13(Rot):
    def encrypt(self, plain_text):
        print("\n")
        print("Selected ROT13!")
        print("\n")
        print("Currently encrypting", plain_text)
        print("\n")
        encrypted_text = codecs.encode(plain_text, "rot_13")
        print("Encrypted successfully!")
        print("Encrypted text:", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        print("\n")
        print("Selected ROT13!")
        print("\n")
        print("Currently decrypting", encrypted_text)
        print("\n")
        decrypted_text = codecs.decode(encrypted_text, "rot_13")
        print("Decrypted successfully!")
        print("Decrypted text:", decrypted_text)
        return decrypted_text
