class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        
        longest = s[0]
        
        # check for odd-length palindromes
        for center in range(len(s)):
            l = center
            r = center
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            l += 1
            r -= 1
            
            longest = s[l : r + 1] if r - l + 1 > len(longest) else longest
        
        # check for even-length palindromes
        for center_l in range(0, len(s) - 1):
            center_r = center_l + 1
            
            if s[center_l] != s[center_r]:
                continue
            
            l = center_l
            r = center_r
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                
            l += 1
            r -= 1
            
            longest = s[l : r + 1] if r - l + 1 > len(longest) else longest
        
        return longest
        
    
class Main:
    sol = Solution()
    
    print(sol.longestPalindrome('aabbcc'))