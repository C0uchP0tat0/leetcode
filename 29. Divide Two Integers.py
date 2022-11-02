class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        if dividend==-2147483648 and divisor==-1:
            result-=1
        return result
        
        
def main():
    dividend = -2147483648
    divisor = -1
    y=Solution()
    y.divide(dividend, divisor)


if __name__ == "__main__":
    main()