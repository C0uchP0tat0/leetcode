class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = x[::-1]
        if x[-1] == "-":
            x = x[-1]+x[:-1]
        x = int(x)
        if x < -2147483648 or x > 2147483648:
            return 0
        return x


if __name__ == "__main__":
    # x = 123
    # Output: 321
    # x = -123
    # Output: -321
    x = 120
    # Output: 21
    obj = Solution()
    print(obj.reverse(x))
