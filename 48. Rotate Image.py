from collections import defaultdict


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        d=defaultdict(list)
        maatrix_rev=list(reversed(matrix))
        for i in maatrix_rev:
            for j in range(len(i)):
                d[j].append(i[j])
        matrix.clear()
        for v in d.values():
            matrix.append(v)


def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    y=Solution()
    y.rotate(matrix)


if __name__ == "__main__":
    main()