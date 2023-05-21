import random
import string
import PyPDF4

class Brute:
    
    def __init__(self, path, length, num_symbols, num_letters, num_numbers):
        self.pdf_path = path
        self.symbols = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.length = length
        self.num_symbols = num_symbols
        self.num_letters = num_letters
        self.num_numbers = num_numbers

    def generate_password(self):
        # make sure the requested password length is greater than the total requested characters
        if self.length < self.num_symbols + self.num_letters + self.num_numbers:
            raise ValueError("Password length must be greater than or equal to the sum of the requested characters.")

        char_list = [random.choice(self.symbols) for _ in range(self.num_symbols)]
        char_list.extend(random.choice(self.letters) for _ in range(self.num_letters))
        char_list.extend(random.choice(self.numbers) for _ in range(self.num_numbers))
        # remove duplicates and pad the list with random characters to reach the desired length
        while len(set(char_list)) < self.length:
            char_list.append(random.choice(string.ascii_letters + string.digits + self.symbols))
        random.shuffle(char_list)
        return "".join(char_list)

    def brute_attack(self, max_attempts=1000000):
        # open the PDF file
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF4.PdfFileReader(pdf_file)

            # check if the PDF file is encrypted
            if pdf_reader.isEncrypted:
                for _ in range(max_attempts):
                    # generate a password
                    password = self.generate_password()
                    # print(password)

                    # try to decrypt the PDF file with the password
                    if pdf_reader.decrypt(password) == 1:
                        return f"Password found: {password}"

                return "Failed to crack the password."

            else:
                return "The PDF file is not encrypted."


