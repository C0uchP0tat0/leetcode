class Solution:
    
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        for i in range(len(nums)):
            try:
                if nums[i]==nums[i+1]:
                    nums[i]='_'
                else:
                    k+=1
            except IndexError:
                k+=1
        for j in nums:
            if j == '_':
                nums.remove(j)
                nums.append(j)
        print(k, nums)


def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    y=Solution()
    y.removeDuplicates(nums)
    
if __name__ == "__main__":
    main()