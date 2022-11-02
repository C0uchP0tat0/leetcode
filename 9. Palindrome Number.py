class Solution:
     def isPalindrome(self, x: int) -> bool:
         x=str(x)
         if x==x[::-1]:
             return True
         else:
             return False
         

def main():
    x = 121
    y=Solution()
    y.isPalindrome(x)
    
if __name__ == "__main__":
    main()