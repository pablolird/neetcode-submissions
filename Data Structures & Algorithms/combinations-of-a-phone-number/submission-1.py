
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
            if not digits:
                return []

            if (index==len(digits)-1):
                d = digits[index]
                for l in map[d]:
                    ans.append(curr+l)

            else:
                d = digits[index]
                for l in map[d]:
                    dfs(index+1, curr+l)
        
        dfs(0, "")
        return ans



        