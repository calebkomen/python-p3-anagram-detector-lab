# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words_list):
        # Sorting the letters of the word initialized
        sorted_word = sorted(self.word)
        # List to hold the anagrams
        anagrams = []
        
        for word in words_list:
            # Check if the sorted letters of the current word match the sorted letters of the initialized word
            if sorted(word) == sorted_word:
                anagrams.append(word)
        
        return anagrams
