class Solution(object):
    def myPow(self, x, n):
        if n==0 :
            return 1.0

        power = abs(n)
        result = 1.0

        while power > 0:
            if power & 1:
                result *= x
            x *= x
            power >>= 1

    
        return result if n > 0 else 1.0/result        