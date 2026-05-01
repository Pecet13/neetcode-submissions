class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        for i in range(n):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break
        return output