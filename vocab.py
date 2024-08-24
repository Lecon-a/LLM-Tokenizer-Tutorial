from whitespace import remove_whitespace

def create_vocab():
    tokens = remove_whitespace()
    tokens.extend(["<|UNK|>", "<|EOF|>"])
    # get distinct tokens
    distinct_tokens = set(tokens)
    vocab = {token:id for id, token in enumerate(distinct_tokens)}
    return vocab

if __name__ == '__main__':
    print(create_vocab())
