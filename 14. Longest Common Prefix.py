class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        pref=[]
        for i in range((len(min(strs)))):
            if len(strs)==1:
                return strs[0]
            else:
                string = strs[0][:1+i]
                for j in strs:
                    if string==j[:1+i]:
                        pref.append(string)
                    else:
                        try:
                            for r in range(len(pref)+1):
                                pref.remove(string)
                        except ValueError:
                            break

        try:
            return max(pref)
        except ValueError:
            return ''


def main():
    strs = ["flower","flow","flight"]
    # strs = ["cir","car"]
    # strs = ["dog","racecar","car"]
    # strs = ["aaa","aa","aaa"]
    # strs = ["a"]
    # strs = ["c","acc","ccc"]
    # strs = ["aba","c","b","a","ab"]
    # strs = ["baab","bacb","b","cbc"]
    y=Solution()
    y.longestCommonPrefix(strs)
    
if __name__ == "__main__":
    main()