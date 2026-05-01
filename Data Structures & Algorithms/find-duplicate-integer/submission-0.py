class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j += 1
        return None