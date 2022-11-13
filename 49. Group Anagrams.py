from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_list=[]
        d=defaultdict(list)

        for string in strs:
            d[str(sorted(string))].append(string)
        for v in d.values():
            strs_list.append(v)
        return strs_list


def main():
    strs = ["ddddddddddg","dgggggggggg"]
    y=Solution()
    y.groupAnagrams(strs)


if __name__ == "__main__":
    main()