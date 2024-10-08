from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        # Сортируем интервалы по начальным значениям
        intervals.sort(key=lambda x: x[0])

        start_value = min(intervals[0][0], intervals[1][0])
        end_value = intervals[0][-1]
        merge_list = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= end_value:
                for j in range(1, len(intervals[i])):
                    if intervals[i][j] < end_value:
                        pass
                    else:
                        end_value = intervals[i][j]
            else:
                merge_list.append([start_value, end_value])
                start_value = intervals[i][0]
                end_value = intervals[i][-1]

        merge_list.append([start_value, end_value])
        return merge_list


if __name__ == "__main__":
    # Example 1:
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # Output: [[1,6],[8,10],[15,18]]
    # Explanation: Since intervals [1,3]
    # and [2,6] overlap, merge them into [1,6].

    # Example 2:
    # intervals = [[1, 4], [4, 5]]
    # Output: [[1,5]]
    # Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    intervals = [[1, 4], [0, 4]]
    # output: [[0,4]]
    obj = Solution()
    print(obj.merge(intervals))
