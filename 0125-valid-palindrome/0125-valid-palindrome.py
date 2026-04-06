class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        
        s = s.lower()
        # Loop until the two pointers meet or cross each other
        while l < r:
        
            # Move left pointer forward until it points to an alphanumeric character
            while not s[l].isalnum() and l < r:
                l += 1
            
            # Move right pointer backward until it points to an alphanumeric character
            while not s[r].isalnum() and l < r:
                r -= 1
            
            # Compare characters 
            if s[l] != s[r]:
                return False  # If mismatch found,
            
            l += 1
            r -= 1
        
        return True