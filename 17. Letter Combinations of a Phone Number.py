class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        number_dict={0:'',1:'', 2:'abc', 3:'def',4:'ghi', 5:'jkl', 6:'mno' ,7:'pqrs', 8:'tuv', 9:'wxyz'}
        letters_list=[]
        try:
            letters=number_dict[int(digits[0])]
        except IndexError:
            return letters_list
        for i in range(len(digits)):
            for l1 in letters:
                try:
                    for l2 in number_dict[int(digits[i+1])]:
                        if len(digits)==2:
                            letters_list.append(l1+l2)
                        else:
                            for l3 in number_dict[int(digits[i+2])]:
                                if len(digits)==3:
                                    letters_list.append(l1+l2+l3)
                                else:
                                    for l4 in number_dict[int(digits[i+3])]:
                                        letters_list.append(l1+l2+l3+l4)
                except IndexError:
                    break
        
        if len(letters_list)==0:
            # print(list(number_dict[int(digits[0])]))
            return list(number_dict[int(digits[0])])
        else:
            # print(letters_list)
            return letters_list


def main():
    digits = "2345"
    y=Solution()
    y.letterCombinations(digits)
    
if __name__ == "__main__":
    main()