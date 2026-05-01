class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        encounters = []
        for n in set(nums):
            encounters.append((n, nums.count(n)))
        res = []
        for m in sorted(encounters, key=lambda elem: elem[1], reverse=True)[:k]:
            res.append(m[0])
        return res
        