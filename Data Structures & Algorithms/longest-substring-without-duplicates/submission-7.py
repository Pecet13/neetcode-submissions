class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_length = 1
        l, r = 0, 0
        seen = set()
        seen.add(s[l])
        while r < len(s) - 1:
            seen.add(s[r])
            r += 1
            if s[r] not in seen:
                seen.add(s[r])
                max_length = max(max_length, len(seen))
            else:
                while s[r] in seen and l < r:
                    seen.remove(s[l])
                    l += 1
        return max_length
