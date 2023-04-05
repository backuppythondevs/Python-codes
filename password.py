import secrets
import string

#  Función que genera una contraseña aleatoria
def PasswordGenerator(length):
    password = ""
    for i in range(length):
        password += secrets.choice(string.ascii_letters
                                   +string.digits+
                                   string.punctuation)
    return password

# BLOQUE PRINCIPAL
if __name__ == "__main__":
    print(PasswordGenerator(10))