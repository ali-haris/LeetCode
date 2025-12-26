class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        needle_lenght = len(needle)
        if needle not in haystack:
            return -1

        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:

                    if haystack[i:i + needle_lenght] == needle:
                        return i


                    






        