import random
import string

def generate_password():
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

    password = []

    while (len(password) < random.randint(16, 20)):
        character=random.choice(characters)
        password.append(character)

    password = "".join(password)
    return password

def run():
    password = generate_password()
    print('Tu nueva contraseña es: '+ password)

if __name__ == "__main__":
    run()