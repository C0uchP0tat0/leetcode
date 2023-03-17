class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        if len(pattern) != len(s.split(' ')):
            return False
        for i, j in zip(pattern, s.split(' ')):
            try:
                if d[i]==j:
                    pass
                else:
                    return False
            except KeyError:
                if j in d.values():
                    return False
                else:
                    d[i]=j
        return True
        
        
def main():
    pattern = "abba"
    s = "dog dog dog dog"
    # Output: false
    y=Solution()
    y.wordPattern(pattern, s)


if __name__ == "__main__":
    main()
