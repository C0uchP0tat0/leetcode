class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_polindrom = ''
        for i in range(len(s)):
            if (len(s)/2)<len(longest_polindrom):
                    return longest_polindrom
            for j in range(len(s)+1):
                if s[i:j]=='':
                    pass
                else:
                    if s[i:j]==s[i:j][::-1]:
                        if len(s[i:j])>len(longest_polindrom):
                            longest_polindrom=s[i:j]
                        else:
                            pass
        # print(longest_polindrom)
        return longest_polindrom
            
            

def main():
    # s = "rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq"
    s = "babad"
    s = "a"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.
    x=Solution()
    x.longestPalindrome(s)
    
if __name__ == "__main__":
    main()