class Cipher:
    """ This Class is to get a string and decrypt it or get a decrypted strings and encrypt it,
        based on provided logic.
    """

    def __init__(self, secret):

        self.secret = secret
        self.encoder = [None]*26
        self.decoder = [None]*26
        self.encoder_lower = [None]*26
        self.decoder_lower = [None]*26

        for i in range(26):
            self.encoder[i] = chr((i + self.secret) % 26 + ord("A"))
            self.decoder[i] = chr((i - self.secret) % 26 + ord("A"))
            self.encoder_lower[i] = chr((i + self.secret) % 26 + ord("a"))
            self.decoder_lower[i] = chr((i - self.secret) % 26 + ord("a"))
        self.encrypt_upper = "".join(self.encoder)
        self.decrypt_upper = "".join(self.decoder)
        self.encrypt_lower = "".join(self.encoder_lower)
        self.decrypt_lower = "".join(self.decoder_lower)

    def convert(self,message):
        """ Take string and convert to encrypted one """
        encrypt_list = []
        for i in message:
            if i.isupper():
                j=ord(i) - ord("A")
                i  = self.encrypt_upper[j]
                encrypt_list.append(i)
            if i.islower():
                    j=ord(i) - ord("a")
                    i  = self.encrypt_lower[j]
                    encrypt_list.append(i)
        return "".join(encrypt_list)


a = Cipher(3)
b = a.convert("AAshu")
print(b)
