
map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        def dfs(index, curr):
            if (index==len(digits)):
                ans.append(curr)
                return

            d = digits[index]
            for l in map[d]:
                dfs(index+1, curr+l)

        if not digits:
            return []

        dfs(0, "")
        return ans



        