class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import sqrt
        return int(x)
            
        
            


def main():
    x = 4
    # Output: 2
    # Explanation: The square root of 4 is 2, so we return 2.
    # x = 8
    # Output: 2
    # Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
    x = 1024
    # x = 2147395599
    y=Solution()
    y.mySqrt(x)


if __name__ == "__main__":
    main()
