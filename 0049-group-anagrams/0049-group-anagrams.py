class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord("a")] += 1
            group[tuple(key)].append(w)
        return list(group.values())



# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = defaultdict(list)
#         result = []

#         for s in strs:
#             sorted_s = tuple(sorted(s))
#             anagram_map[sorted_s].append(s)

#         for value in anagram_map.values():
#             result.append(value)

#         return result