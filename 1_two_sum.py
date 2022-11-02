def get_result(nums, target):
    l=list()
    len_nums = len(nums)
    indexes_list=[i for i in range(len_nums)]
    d_nums = dict(zip(indexes_list, nums))
    for i in d_nums:
        for k in range(1,len_nums):
            try:
                z=d_nums[i+k]
            except KeyError:
                continue
            if d_nums[i]+z==target:
                l.append(i)
                l.append(i+k)
                return l
    

def main():
    nums = [2,7,11,15]
    target =9
    get_result(nums, target)
    
if __name__ == "__main__":
    main()