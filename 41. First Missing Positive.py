class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        l = [n for n in sorted(set(nums)) if n>0]
        if len(l)<1:
            return 1
        for i in range(len(l)):
            try:
                if l[0]>1:
                    return 1
                elif l[i]+1==l[i+1]:
                    continue
                else:
                    return l[i]+1
            except IndexError:
                return l[i]+1


def main():
    nums = [0]
    y=Solution()
    y.firstMissingPositive(nums)


if __name__ == "__main__":
    main()