from src.utils.Rot import Rot


class ROT47(Rot):
    def encrypt(self, plain_text):
        print("\n")
        print("Selected ROT47!")
        print("\n")
        print("Currently encrypting", plain_text)
        print("\n")
        encode = []
        for i in range(len(plain_text)):
            j = ord(plain_text[i])
            if 33 <= j <= 126:
                encode.append(chr(33 + ((j + 14) % 94)))
            else:
                encode.append(plain_text[i])
        encrypted_text = "".join(encode)
        print("Encrypted successfully!")
        print("Encrypted text:", encrypted_text)
        return encrypted_text

    def decrypt(self, encrypted_text):
        print("\n")
        print("Selected ROT47!")
        print("\n")
        print("Currently decrypting", encrypted_text)
        print("\n")
        decode = []
        for i in range(len(encrypted_text)):
            encoded = ord(encrypted_text[i])
            if encoded >= 33 and encoded <= 126:
                decode.append(chr(33 + ((encoded + 14) % 94)))
            else:
                decode.append(encrypted_text[i])
        decrypted_text = "".join(decode)
        print("Decrypted successfully!")
        print("Decrypted text:", decrypted_text)
        return decrypted_text
