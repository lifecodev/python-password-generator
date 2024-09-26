import random
import string


def gen_password(length: int, include_digits: bool = True, include_punctuation: bool = True) -> str:

    password = ""
    letters_str = string.ascii_letters

    if include_digits:
        letters_str += string.digits
    if include_punctuation:
        letters_str += string.punctuation

    for i in range(length):
        rand_int = random.randrange(0, len(letters_str))
        password += letters_str[rand_int]
    return password


if __name__ == '__main__':
    print(gen_password(10, include_punctuation=False))
