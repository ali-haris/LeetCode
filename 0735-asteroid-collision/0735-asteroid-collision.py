class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:  # Fixed spelling
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:         # Current asteroid is bigger → pop stack asteroid
                    stack.pop()
                    continue         # Check further collisions
                elif diff > 0:       # Stack asteroid is bigger → current dies
                    a = 0
                else:                # Equal size → both die
                    a = 0
                    stack.pop()
                break  # Exit while loop if current asteroid is destroyed
            
            if a:  # If asteroid still alive, push to stack
                stack.append(a)
        
        return stack  # Return after processing all asteroids