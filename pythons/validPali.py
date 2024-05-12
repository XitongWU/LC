class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        if len(s) == 1:
            return True
        s = s.lower()
        while(left <= right):
            if (s[left].isalpha() or s[left].isdigit()) is True and (s[right].isalpha() or s[right].isdigit() is True):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            
            else:
                    
                if s[left].isalpha() is False and s[left].isdigit() is False:
                    left += 1
                if s[right].isalpha() is False and s[right].isdigit() is False:
                    right -= 1
                
        return True
            
            
            
        pass