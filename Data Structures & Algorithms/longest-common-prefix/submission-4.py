class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Outer: Iterate each word strs[i] using for loop starting at the second word
        # 1. Saving the prefix as the first word
        # 2. Inner: Check WHILE the index j still within the minimum length 
        # between that word strs[i] and the prefix
        #   a. If that letter is different than the prefix at that position j, break the loop
        #   b. else: move j to the next position. 
        # 3. Update the prefix from the index 0 to index j 
        # 4. Return that prefix 
        # Time complexity: O(n) and n represent for total characters of a string
        if len(strs) == 1: return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs), 1):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if strs[i][j] != prefix[j]:
                    break
                j+=1
            prefix = prefix[:j]
            # Early exit: if prefix is empty, no point comparing more words
            if prefix == "":
                return prefix
        return prefix

