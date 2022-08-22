from src.utils.Rot import Encrypt


class ROT47(Encrypt):

    def encrypt(self, plain_text):
        print("\n")
        print('Selected ROT47!')
        print("\n")
        print('Currently encrypting', plain_text)
        print("\n")
        x = []
        for i in range(len(plain_text)):
            j = ord(plain_text[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(plain_text[i])
        encrypted_text = ''.join(x)
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)
        return encrypted_text
