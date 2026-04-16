class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length
        if len(s) == 0 or len(t)==0: return False
        if len(s) != len(t) : return False
        # Create 2 dict 
        dict_s, dict_t = {}, {}
        for letter in s:
            dict_s[letter] = 1 + dict_s.get(letter, 0)
        for letter in t:
            dict_t[letter] = 1 + dict_t.get(letter, 0)
        # Compare the counter
        print(dict_s)
        print(dict_t)
        for letter in dict_s:
            if letter not in dict_t or dict_s[letter] != dict_t[letter]:
                return False
        return True
        