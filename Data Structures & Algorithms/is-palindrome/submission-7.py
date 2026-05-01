class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            while (not s[i].isalnum() or s[i] == ' ') and i < len(s) - 1:
                i += 1
            while (not s[j].isalnum() or s[j] == ' ') and j > 0:
                j -= 1
            if s[i].isalnum() and s[j].isalnum() and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True