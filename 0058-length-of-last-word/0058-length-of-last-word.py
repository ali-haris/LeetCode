class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[-1]

        no_words = 0

        for letter in last_word:
            no_words +=1

        return no_words


        