from collections import defaultdict


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        d=defaultdict(list)
        for i in range(rowIndex+2):
            for j in range(i):
                if i<=2:
                    d[i].append(1)
                else:
                    if j==0 or j==i-1:
                        d[i].append(1)
                    else:
                        l=d[i-1][j-1:j+1]
                        d[i].append(l[0]+l[-1])
        print(d[rowIndex+1])
        return d[rowIndex+2]


def main():
    rowIndex = 3
    # Output: [1,3,3,1]
    y=Solution()
    y.getRow(rowIndex)


if __name__ == "__main__":
    main()