import PyPDF4


class PDFcrack:

    def __init__(self, path, password_list):
        self.pdf_path = path
        self.password_list = password_list

    def crack(self):
        with open (self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF4.PdfFileReader(pdf_file)
            if pdf_reader.isEncrypted:
                for pw in self.password_list:
                    if pdf_reader.decrypt(pw) == 1:
                        return f"{pw}"
                return "Faild to crack the password"
            else:
                return "The pdf file is not encrypted"
                