class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        s = set([i for i in range(n+1)])
        nums = set(nums)
        return (s-nums).pop()


def main():
    # nums = [3,0,1]
    # Output: 2
    # Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
    nums = [9,6,4,2,3,5,7,0,1]
    # Output: 8
    # Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
    y=Solution()
    y.missingNumber(nums)


if __name__ == "__main__":
    main()
