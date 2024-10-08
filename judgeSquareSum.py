class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)

        while a <= b:
            sum =  a*a + b*b    
            if sum < c:
                a += 1
            elif sum > c:
                b -= 1
            else:
                return True
        return False    
        
