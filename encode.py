import re
from vocab import create_vocab
from tokenize import tokenize
from whitespace import remove_whitespace


vocab = create_vocab()
print(vocab)

def encode():
    realtime_input = input("Enter your text: ")
    _input = re.split(r"([.,!\’”:;?()}{_]|--|-|\s)", realtime_input)
    _input = [token for token in _input if token.strip()]
    encoded_text = []
    for word in _input:
        if word in vocab.keys():
            encoded_text.append(vocab[word])
        else:
            word = "<|UNK|>"
            encoded_text.append(vocab[word])
    return encoded_text

def decode(indexes):
    reversed_vocab = {value:key for key, value in vocab.items()}
    decoded_ids = [reversed_vocab[id] for id in indexes]
    return decoded_ids

def concatenate_the_decoded_ids(decoded_ids):
    return " ". join(decoded_ids)


if __name__ == "__main__":
    encoded_text = encode()
    print("Encoded Text: ",encoded_text)
    decoded_ids = decode(encoded_text)
    print("Decoded Indexes: ", decoded_ids)
    print("Back to user input: ", concatenate_the_decoded_ids(decoded_ids))