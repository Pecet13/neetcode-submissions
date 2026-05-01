class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}
        nums = sorted(set(nums))
        for num in nums:
            if num - 1 not in nums:
                sequences[num] = 1
            else:
                i = num
                while (i in nums and i not in sequences.keys()):
                    i -= 1
                sequences[i] += 1
        if len(sequences.keys()) == 0:
            return 0
        return max(sequences.values())