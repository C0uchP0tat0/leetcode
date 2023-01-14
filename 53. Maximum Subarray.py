class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # initial
        answer = nums[0]
        temp_sum = nums[0]
        # loop
        for i in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            if temp_sum > answer:
                answer = temp_sum
        return answer
        
        
def main():
    nums = [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1,-93,42,44,1,-75,-25,-87,\
        -16,9,-59,20,5,-95,-41,4,-30,47,46,78,52,74,93,-3,53,17,34,-34,34,-69,-21,-87,\
            -86,-79,56,-9,-55,-69,3,5,16,21,-75,-79,2,-39,25,72,84,-52,27,36,98,20,-90,52,\
                -85,44,94,25,51,-27,37,41,-6,-30,-68,15,-23,11,-79,93,-68,-78,90,11,-41,-8,-17]
    y=Solution()
    y.maxSubArray(nums)


if __name__ == "__main__":
    main()