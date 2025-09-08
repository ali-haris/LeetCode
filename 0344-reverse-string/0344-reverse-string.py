class Solution:
    # def reverseString(self, s: List[str]) -> None:
    #     def helper(left: int, right: int) -> None:
    #         # Base case
    #         if left >= right:
    #             return
            
    #         # Swap
    #         s[left], s[right] = s[right], s[left]
            
    #         # Recursive step
    #         helper(left + 1, right - 1)
        
    #     # Initial call
    #     helper(0, len(s) - 1)
        
   # normal     
    def reverseString(self,s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        # Swap characters from both ends moving towards the middle
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap
            left += 1
            right -= 1