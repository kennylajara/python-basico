def palindrome( word ):
    word = word.replace(' ', '') # delete spaces
    word = word.lower() # string to lower
    return word == word[::-1]


def run():
    word =  input("Escribe una palabra o frase: ")
    is_palindrome = palindrome( word )
    if is_palindrome == True:
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")


if __name__ == "__main__":
    run()