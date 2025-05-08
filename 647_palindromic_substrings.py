# Given a string s, return the number of palindromic substrings in it.

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not len(s):
            return 0
        
        count = 0
        
        # count odd-length palindromes
        for center in range(len(s)):
            l = center
            r = center
            
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
        
        for center_l in range(len(s) - 1):
            center_r = center_l + 1
            
            l = center_l
            r = center_r
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count