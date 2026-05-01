class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            mid = math.ceil((l + r)/2)
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return nums[l]
