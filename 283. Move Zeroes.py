class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            try:
                nums.remove(0)
                nums.append(0)
            except ValueError:
                pass
        

def main():
    nums = [0,0,1]
    # Output: [1,3,12,0,0]
    y=Solution()
    y.moveZeroes(nums)


if __name__ == "__main__":
    main()
