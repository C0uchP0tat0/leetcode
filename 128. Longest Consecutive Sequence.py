class Solution:
        
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        output=1
        nums=sorted(nums)
        output_mid=1
        for i in range(len(nums)):
            try:
                if nums[i]+1==nums[i+1]:
                    output_mid+=1
                    if output_mid>output:
                        output=output_mid
                elif nums[i]==nums[i+1]:
                    pass
                else:
                    output_mid=1
            except IndexError:
                pass
        return output


def main():
    # nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    # nums = [1,2,0,1]
    # Output: 4
    # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    y=Solution()
    y.longestConsecutive(nums)


if __name__ == "__main__":
    main()
