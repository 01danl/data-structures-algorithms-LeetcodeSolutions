class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        d = {}

        for res in responses:
            for c in set(res):
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 0
        
        max_val = max(d.values())

        res = [word for word, value in d.items() if value == max_val]

        return min(res)
