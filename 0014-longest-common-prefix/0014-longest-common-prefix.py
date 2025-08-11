class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Loop through each character index of the first word
        for i in range(len(strs[0])):
            # Get the character at index i in the first word
            char = strs[0][i]
            
            # Compare it with the same index in all other words
            for s in strs[1:]:
                # If index i is out of range or characters don't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]  # Return common prefix up to index i

        # If no mismatch found, entire first word is the prefix
        return strs[0]