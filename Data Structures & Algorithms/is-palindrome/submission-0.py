class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Join the input by removing the space.
        # Compare each character in left at 0th index and right pointer at the (len(s)-1) while left < right
        # if the characters of left and right pointer in the same lower capitalization is different, return false.
        # Otherwise return true

        left, right = 0, len(s) -1 
        newStr = ''.join(s)
        while left <= right:
            while not newStr[left].isalnum(): 
                left += 1
            while not newStr[right].isalnum(): 
                right -= 1     
            if newStr[left].lower() != newStr[right].lower():
                return False
            left += 1
            right -= 1
        return True