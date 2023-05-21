import PyPDF4


class PDFcrack:

    def __init__(self, path, password_list):
        self.pdf_path = path
        self.password_list = password_list

    def crack(self):
        with open (self.pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF4.PdfFileReader(pdf_file)
            if pdf_reader.isEncrypted:
                return next(
                    (
                        f"{pw}"
                        for pw in self.password_list
                        if pdf_reader.decrypt(pw) == 1
                    ),
                    "Faild to crack the password",
                )
            else:
                return "The pdf file is not encrypted"
                