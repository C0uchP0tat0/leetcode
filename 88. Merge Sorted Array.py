class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(len(nums1), -1, -1):
            if i<m:
                pass
            elif i>=m-1:
                try:
                    nums1.pop(i)
                except IndexError:
                    pass
        for j in range(len(nums2)):
            if j<n:
                nums1.append(nums2[j])
            else:
                return
        nums1.sort()
        print(nums1)
        
        
def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    y=Solution()
    y.merge(nums1, m, nums2, n)


if __name__ == "__main__":
    main()