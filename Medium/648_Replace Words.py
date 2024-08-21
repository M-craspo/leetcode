class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        dictionary = ["cat","bat","rat"], 
        sentence = "the cattle was rattled by the battery"
        """
        words = sentence.split()
        for i in dictionary:
            for _ in range(len(words)) :
                if words[_].startswith(i) :
                    words[_] = i
        return ' '.join(words) 

s = Solution()
print(s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
