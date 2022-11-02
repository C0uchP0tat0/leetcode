class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_list=nums1+nums2
        res_list = sorted(res_list)
        len_res_list = len(res_list)/2
        if len(res_list)%2==0:
            print(sum(res_list[int(len_res_list-1):int(len_res_list+1)])/2)
        else:
            print(res_list[int(len_res_list-0.5)])


def main():
    nums1 = [1,3]
    nums2 = [2, 4]
    x=Solution()
    x.findMedianSortedArrays(nums1, nums2)
    
if __name__ == "__main__":
    main()