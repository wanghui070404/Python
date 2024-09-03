import random
import string


def generate_key():
    characters = list(string.ascii_lowercase)
    random.shuffle(characters)
    return ''.join(characters)


def substitution_encrypt(text, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return text.translate(table)


def substitution_decrypt(text, key):
    table = str.maketrans(key, string.ascii_lowercase)
    return text.translate(table)


if __name__ == "__main__":
    key = generate_key()
    for i in range(26):
        print(string.ascii_lowercase[i], "=", key[i])
    text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming"
    cipher = substitution_encrypt(text, key)
    print("Cipher: ", cipher)
    plantext = substitution_decrypt(text, key)
    print("Plantext: ", plantext)
