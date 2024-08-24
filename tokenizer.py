# import necessary libraries
import re

class SPaTokenizer:
    '''
    TODO:
    - Read in text document for building vocab
    - Tokenize text document
    - Remove the whitespace
    - Create vocabulary
    - Implement encode method
    - Implement decode method
    - print the user input
    '''
    def __init__(self):
        self.file = None
        self.tokens = []
        self.vocab = {}

    def __repr__(self) -> str:
        return f"<File Input: {self.file} >"

    def read_in_document(self, file_path):
        try:
            with open(file_path, 'r') as f:
                self.file = f.read()    
        except FileNotFoundError as e:
            raise FileNotFoundError("file or directory is not found: '{}'".format(file_path))

    def tokenize(self):
        words = re.split(r"([.,!\’”:;?()}{_]|--|-|\s)", self.file)
        self.tokens = self.remove_whitespace(words)


    def remove_whitespace(self, chunks):
        return [token for token in chunks if token.strip()]

    def create_vocab(self):
        self.tokens.extend(["<|UNK|>", "<EOF>"])
        # get distinct tokens
        self.tokens = set(self.tokens)
        self.vocab = {token:id for id, token in enumerate(self.tokens)}

    def encode(self, prompt):
        def tokenize(text):
            return re.split(r"([.,!\’”:;?()}{_]|--|-|\s)", text)
        prompt = tokenize(prompt)
        prompt = self.remove_whitespace(prompt)
        encoded_prompt = [
            self.vocab[chunk] 
            if chunk in self.vocab.keys() 
            else self.vocab["<|UNK|>"]
            for chunk in prompt
        ]
        return encoded_prompt

    def decode(self, encoded_text):
        reversed_vocab = {value:key for key, value in self.vocab.items()}
        return [reversed_vocab[id] for id in encoded_text]

    # Assignment
    def print_decode_value(self):
        pass


# This is to instantiate a tokenizer object
tokenizer = SPaTokenizer()
tokenizer.read_in_document("sample.txt")
tokenizer.tokenize()
tokenizer.create_vocab()
user_query = input("Enter your query here: ")
encoded_text = tokenizer.encode(user_query)
print("Encoded User query: ", encoded_text)
decoded_text = tokenizer.decode(encoded_text)
print("Decode the encoded user query: ", decoded_text)



