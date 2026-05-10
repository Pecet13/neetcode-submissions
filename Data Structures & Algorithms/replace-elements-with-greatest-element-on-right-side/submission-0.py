class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = 0
        for i in range(len(arr)-1, -1, -1):
            arr[i], highest = highest, max(highest, arr[i])
        arr[-1] = -1
        return arr
