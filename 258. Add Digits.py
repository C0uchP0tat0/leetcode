class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        if len(str(num)) == 1:
            return num
        else:
            num = sum([int(n) for n in str(num)])
            num = self.addDigits(num)
        return num
        
        
        
def main():
    num = 38
    # Output: 2
    y=Solution()
    y.addDigits(num)


if __name__ == "__main__":
    main()
