class Solution:
    def __init__(self):
        self.l=[]
        self.count=0

        
    def trap(self, height: list[int]) -> int:
        num_blocks = 0
        n = 0
        max_height = float('-inf')
    
        # Find total blocks, max height and length of array
        for h in height:
            num_blocks += h
            n += 1
            max_height = max(max_height, h)
    
        # Total water, left pointer and right pointer 
        # initialized to 0 and n - 1
        total = 0
        left = 0
        right = n - 1
    
        for i in range(1, max_height+1):
            
            # Find leftmost point greater than current row (i)
            while height[left] < i:
                left += 1
            
            # Find rightmost point greater than current row (i)
            while height[right] < i:
                right -= 1
            
            # Water in this row = right - left + 1
            total += (right - left + 1)
        
        total -= num_blocks
        return total

                
            
            
            


def main():
    height = [0,1,0,2,1,0,1,2,2,1,2,1]
    height = [4,2,0,3,2,5]
    y=Solution()
    y.trap(height)


if __name__ == "__main__":
    main()