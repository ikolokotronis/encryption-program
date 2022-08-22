import codecs


class ROT13(Encrypt):

    def encrypt(self, plain_text):
        print("\n")
        print('Selected ROT13!')
        print("\n")
        print('Currently encrypting', plain_text)
        print("\n")
        encrypted_text = codecs.encode(plain_text, 'rot_13')
        print('Encrypted successfully!')
        print('Encrypted text:', encrypted_text)
        return encrypted_text
