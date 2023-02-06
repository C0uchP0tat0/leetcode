from collections import defaultdict
import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        d=defaultdict(list)
        answer=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    pass
                else:
                    d[i].append(nums[j])
        for v in d.values():
            answer.append(math.prod(v))
        # print(answer)
        # print(d)
        return answer
        

def main():
    # nums = [1,2,3,4]
    nums = [0,0]
    # Output: [24,12,8,6]
    y=Solution()
    y.productExceptSelf(nums)


if __name__ == "__main__":
    main()
