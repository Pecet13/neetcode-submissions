class PrefixTree:

    def __init__(self):
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return len(self.words) != 0 and \
            any(len(prefix) <= len(word) and prefix == word[:len(prefix)] for word in self.words)
        