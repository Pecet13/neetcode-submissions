class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        ls, rs = [], []
        l_max, r_max = -1, 0
        
        for i in range(len(height)):
            if r_max < i:
                r = i
                r_max = i
                while r < len(height):
                    if height[r] > height[r_max]:
                        r_max = r
                    r += 1
            rs.append(height[r_max])
        
        for j in range(1, len(height)+1):
            if l_max > -j:
                l = -j
                l_max = -j
                while l > -len(height) - 1:
                    if height[l] > height[l_max]:
                        l_max = l
                    l -= 1
            ls.append(height[l_max])
        
        for k in range(len(height)):
            res += min(ls[-k-1], rs[k]) - height[k]
            
        return res