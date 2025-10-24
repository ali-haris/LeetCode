from itertools import permutations
from functools import reduce
from bisect    import bisect_right
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if  n==0:  return 1
        perm = [[[]],[[]],[[]],
            [[1,2,2]],
            [[1,3,3,3]],
            [[1,4,4,4,4],[2,2,3,3,3]],
            [[1,2,2,3,3,3],[1,5,5,5,5,5],[2,2,4,4,4,4]]
        ]
        ctab = [[0],[1],[22],[333],[4444],[55555],[666666],[1224444]]
        for i in range(3,7):
            for numset in perm[i]:
                ctab[i].extend({reduce(lambda x,y: x*10+y, lst)
                    for lst in permutations(numset)
                })
            ctab[i].sort()
        pow = 7
        while not n//10**(pow-1): pow -= 1
        idx = bisect_right(ctab[pow], n)
        #print(pow, idx, ctab[pow])
        return  ctab[pow][idx] if  idx<len(ctab[pow])  else ctab[pow+1][0]

        