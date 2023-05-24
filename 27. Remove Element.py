class Solution(object):
    def __init__(self):
        self.counter=0

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
                self.counter+=1
                self.removeElement(nums, val)
        return len(nums)-self.counter


def main():
    # nums = [3,2,2,3]
    # val = 3
    # Output: 2, nums = [2,2,_,_]
    # Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    # It does not matter what you leave beyond the returned k (hence they are underscores).
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    # Output: 5, nums = [0,1,4,0,3,_,_,_]
    # Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
    # Note that the five elements can be returned in any order.
    # It does not matter what you leave beyond the returned k (hence they are underscores).
    y=Solution()
    y.removeElement(nums, val)
    


if __name__ == "__main__":
    main()
