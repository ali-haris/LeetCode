class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        n=len(bits)
        # as two bits is only start with 1 10 or 11 not 00 or 01
        while i<n-1:
            i+=bits[i]+1 # if start with 1 then jump 2 else 1
        return i==n-1