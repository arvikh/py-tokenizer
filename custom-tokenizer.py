import random
class SimpleTokenizer:
    def __init__(self):
        self.char_to_index = {}
        self.index_to_char = {}
        self.next_index = random.randint(1000,9999)

    def encode(self, text):
        tokens = []
        for char in text.split():
            if char not in self.char_to_index:
                self.char_to_index[char] = self.next_index
                self.index_to_char[self.next_index] = char
                self.next_index = random.randint(1000,9999)
            tokens.append(self.char_to_index[char])
        return tokens

    def decode(self, tokens):
        text = ""
        for token in tokens:
            if token in self.index_to_char:
                text += self.index_to_char[token]
        return text

tokenizer = SimpleTokenizer()
text = "Hello, World!"
encoded = tokenizer.encode(text)
print(f"Encoded: {encoded}")
decoded = tokenizer.decode(encoded)
print(f"Decoded: {decoded}")
