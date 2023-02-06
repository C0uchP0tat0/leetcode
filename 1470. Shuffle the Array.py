class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i+(n)])
        return answer
        # print(answer)
        
        
def main():
    nums = [2,5,1,3,4,7]
    n = 3
    # Output: [2,3,5,4,1,7]
    y=Solution()
    y.shuffle(nums, n)


if __name__ == "__main__":
    main()
