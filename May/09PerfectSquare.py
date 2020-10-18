class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left=2
        right=num//2
        while left <= right:
            x=left+(right-left)//2
            guess_square=x*x
            if guess_square == num:
                return True
            if guess_square > num:
                right=x-1
            else:
                left=x+1
        return False
        