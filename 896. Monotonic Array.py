class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sort_nums=sorted(nums)
        if sort_nums==nums:
            return True
        else:
            sort_nums.reverse()
            if sort_nums==nums:
                return True
        return False


def main():
    # nums = [1,2,2,3]
    # Output: true
    nums = [6,5,4,4]
    # Output: true
    # Input: nums = [1,3,2]
    # Output: false
    y=Solution()
    y.isMonotonic(nums)


if __name__ == "__main__":
    main()