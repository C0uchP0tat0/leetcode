class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
        

def main():
    x = 2.0
    n = -2
    y=Solution()
    y.myPow(x, n)


if __name__ == "__main__":
    main()