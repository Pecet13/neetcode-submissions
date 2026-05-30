class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            for word in dictionary:
                if i + len(word) > len(s):
                    continue

                if s[i:i+len(word)] == word:
                    res = min(res, dfs(i + len(word)))
                
            dp[i] = res
            return res
        
        return dfs(0)
