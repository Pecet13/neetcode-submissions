class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        if target <= nums[len(nums)-1]:
            r = len(nums)-1
        else:
            r = max(l - 1, 0)
            l = 0
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
