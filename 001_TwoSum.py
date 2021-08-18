# -*- coding: utf-8 -*-
# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sort = sorted(nums)
        beforeNum = 0
        answer = []
        for i in nums_sort:
            if i < target:
                if i + beforeNum == target:
                    index = nums.index(beforeNum)
                    answer.append(index)
                    answer.append(index + 1)
                    return answer
                else:
                    beforeNum = i


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
