class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(-31, 32):
            if 2 ** i == n:
                return True
        return False
        
        

def main():
    n = 1
    # Output: true
    y=Solution()
    y.isPowerOfTwo(n)


if __name__ == "__main__":
    main()
