from collections import defaultdict


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        d=defaultdict(list)
        for i in range(numRows+1):
            for j in range(i):
                if i<=2:
                    d[i].append(1)
                else:
                    if j==0 or j==i-1:
                        d[i].append(1)
                    else:
                        l=d[i-1][j-1:j+1]
                        d[i].append(l[0]+l[-1])
        return d.values()


def main():
    numRows = 5
    # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    y=Solution()
    y.generate(numRows)


if __name__ == "__main__":
    main()