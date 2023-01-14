class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        # a=bin(int(a))
        # b=bin(int(b))
        # print(a+b)
        # print(str(bin(a+b)))
        return str(bin(a+b))[2:]
        
def main():
    a='11'
    b='1'
    y=Solution()
    y.addBinary(a, b)


if __name__ == "__main__":
    main()