class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def odds_up_to(x: int) -> int:
            return (x + 1) // 2
        
        return odds_up_to(high) - odds_up_to(low - 1)