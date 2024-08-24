from tokenize import tokenize

def remove_whitespace():
    tokens = tokenize()
    cleaned_tokens = [token for token in tokens if token.strip()]
    return cleaned_tokens


if __name__ == '__main__':
    print(remove_whitespace())