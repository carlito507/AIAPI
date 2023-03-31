import tiktoken


class Tokenizer:
    def __init__(self, encoding_name: str = "cl100k_base", for_model: bool = False):
        self.encoding_name = encoding_name
        if for_model:
            self.enc = tiktoken.encoding_for_model(encoding_name)
        else:
            self.enc = tiktoken.get_encoding(encoding_name)

    def get_encoding(self):
        return self.enc

    def encode(self, text):
        return self.enc.encode(text)

    def decode(self, text):
        return self.enc.decode(text)

    def decode_single_token(self, token):
        return self.enc.decode_single_token_bytes(token)

