class Solution:
    def __init__(self) -> None:
        self.cur_list=[]
        
    def generateParenthesis(self, n: int) -> list[str]:
        self.generate("", 0, 0, n)
        return self.cur_list
        
    def generate(self, cur, open, closed, n):
        if len(cur)==2*n:
            self.cur_list.append(cur)
        if open<n:
            self.generate(cur+'(', open+1, closed, n)
        if closed<open:
            self.generate(cur+')', open, closed+1, n)


def main():
    n=3
    y=Solution()
    y.generateParenthesis(n)
    
if __name__ == "__main__":
    main()