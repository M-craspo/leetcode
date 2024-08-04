class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        x = word[0:word.index(ch)+1]
        y = x[::-1] + word[word.index(ch)+1 :]
        return y