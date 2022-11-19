class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_rev=s.split(' ')[::-1]
        for i in s_rev:
            if i=='':
                pass
            else:
                return len(i)
            
        
        
def main():
    s = "   fly me   to   the moon  "
    y=Solution()
    y.lengthOfLastWord(s)


if __name__ == "__main__":
    main()