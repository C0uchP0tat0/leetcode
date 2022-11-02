class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        else:
            return -1


def main():
    haystack = "leetcode"
    needle = "leeto"
    y=Solution()
    y.strStr(haystack, needle)


if __name__ == "__main__":
    main()