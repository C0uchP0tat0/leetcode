from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            res += [subset + [x] for subset in res]
        return res

if __name__ == "__main__":
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    # Example 2:

    # Input: nums = [0]
    # Output: [[],[0]]

    solution = Solution()
    nums = [9,0,3,5,7]
    result = solution.subsets(nums)
