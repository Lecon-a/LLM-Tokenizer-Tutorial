import re
from input import user_input

def tokenize():
    # return user_input.split(" ")
    return re.split(r"([.,!\’”:;?()}{_]|--|-|\s)", user_input)

if __name__ == '__main__':
    # print("Print inside tokenize file: ", user_input)
    print("Raw Text: ", user_input)
    print("Tokes | Words: ", tokenize())