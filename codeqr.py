from qrcode import make

class CodeQR:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def generateQr(self):
        make(self.data).save(self.file_name)

if __name__ == '__main__':
    data = 'https://instagram.com/backup_python.dev'
    file_name = 'MyCodeQR.png'
    code_qr = CodeQR(data, file_name)
    code_qr.generateQr()



