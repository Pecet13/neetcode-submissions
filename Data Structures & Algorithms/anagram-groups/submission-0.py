class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for s in strs:
            added = False
            for sublist in output:
                for t in sublist:
                    if sorted(t) == sorted(s):
                        sublist.append(s)
                        added = True
                        break
            if not added:
                output.append([s])
        return output