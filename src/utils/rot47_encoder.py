def rot47_encoder(buffer):
    x = []
    for i in range(len(buffer)):
        j = ord(buffer[i])
        if 33 <= j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(buffer[i])
    encrypted_text = ''.join(x)
    return encrypted_text
