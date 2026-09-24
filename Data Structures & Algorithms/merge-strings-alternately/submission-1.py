class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       altorder = []
       looplen = max(len(word1), len(word2))
       for i in range(looplen):
        if i < len(word1):
            altorder.append(word1[i])
        if i < len(word2):
            altorder.append(word2[i])
       return ''.join(altorder)
       
            