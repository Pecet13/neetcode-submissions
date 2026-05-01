class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f'{len(s)}ą{s}'
        return res

    def decode(self, s: str) -> List[str]:
        output = []
        begin = 0
        for i in range(len(s)):
            if s[i] == 'ą':
                length = int(s[begin:i])
                begin = i + length + 1
                output.append(s[i+1:begin])
        return output
                
