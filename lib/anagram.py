class Anagram:
    def _init_(self, word):
        self.word = word

    def match(self, words):
        return [w for w in words if sorted(w.lower()) == sorted(self.word.lower()) and w.lower() != self.word.lower()]