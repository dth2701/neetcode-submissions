class Solution:
    "neet", "co#de"
    "24#neet5#co#de"
    def encode(self, strs: List[str]) -> str:
    # Add count and # after length
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Number can have >= 1 digits, like 25, 343
            digits = i
            while s[digits] != "#":
                digits += 1
            length = int(s[i:digits])
            # Adding word
            word = s[digits+1:digits+1+length]
            result.append(word)
            # Moving the pointer to the next word 
            i = digits+1+length
        return result


