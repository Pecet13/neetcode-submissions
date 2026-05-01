class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    valid = [nums[i], nums[j], nums[k]]
                    if valid not in output:
                        output.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1
        return output