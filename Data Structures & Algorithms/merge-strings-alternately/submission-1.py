class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left =  0
        result = ""
        while left < len(word1) and left < len(word2):
            result += word1[left] + word2[left]
            left += 1

        # Out of bound
        if left < len(word1):
            result += word1[left:]
        elif left < len(word2):
            result += word2[left:]
        
        return result