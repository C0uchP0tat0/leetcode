class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_polindrom = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longest_polindrom) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    longest_polindrom = s[i:j]

        print(longest_polindrom)
            
            

def main():
    s = "rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq"
    x=Solution()
    x.longestPalindrome(s)
    
if __name__ == "__main__":
    main()