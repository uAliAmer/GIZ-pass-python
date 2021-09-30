

class Solution:

    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            if s is "":
                return False
            for i in range(len(s)//2):
                if s[i] != s[-1-i]:
                    return False
            return True
        common_subs = {}
        
        if s is "":
            return ""
            
        for i in range(len(s)):
            for j in range(1, len(s)+1):
                if isPalindrome(s[i:j]):
                    common_subs[s[i:j]] = len(s[i:j])
        
        return max(common_subs, key=common_subs.get)