class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result_list=[]
        d=''.join(map(str, digits))
        d=int(d)+1
        for i in str(d):
            result_list.append(int(i))
        # print(result_list)
        return result_list
        
def main():
    digits = [9,9]
    y=Solution()
    y.plusOne(digits)


if __name__ == "__main__":
    main()