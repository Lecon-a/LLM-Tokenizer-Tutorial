# Loading Raw Text:

# Entering through terminal
# user_input = input('Enter your text here: ')
# print("Here is what you entered: ", user_input)

# Reading Raw Text through open method
with open("sample.txt", "r") as file:
    user_input = file.read()

if __name__ == "__main__":
    print("Here is what is in the file: ", user_input)