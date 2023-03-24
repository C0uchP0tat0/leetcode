class Solution:
    def maxArea(self, height: list[int]) -> int:
        liters = 0
        leng = len(height)
        for i in range(leng):
            for j in range(i+1, leng):
                lenght = j-i
                i_or_j = min(height[i], height[j])
                liters = max(liters, i_or_j*lenght)
        return liters
        
                
                
            
        
        
        
def main():
    height = [1,8,6,2,5,4,8,3,7]
    # height = [2,3,10,5,7,8,9]
    # height = [2,3,4,5,18,17,6]
    # height = [4,3,2,1,4]
    # height = [1,1]
    # Output: 49
    # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. \
        # In this case, the max area of water (blue section) the container can contain is 49.
    y=Solution()
    y.maxArea(height)


if __name__ == "__main__":
    main()
