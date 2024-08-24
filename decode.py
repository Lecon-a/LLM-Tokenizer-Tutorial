from vocab import create_vocab

vocab = create_vocab()
print(vocab)

def decode():
    idx2tokens = {id:token for id, token in vocab.items()}
    return idx2tokens

if __name__ == '__main__':
    print(decode())