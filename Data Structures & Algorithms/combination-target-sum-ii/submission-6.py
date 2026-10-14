class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(curr, sum, index):
            if (index==len(candidates) or sum>target):
                return
                        
            curr.append(candidates[index])

            if (sum+candidates[index]==target):
                ans.append(curr.copy())

            dfs(curr, sum+candidates[index], index+1)
            curr.pop()

            prev = candidates[index]
            while (index < len(candidates) and prev==candidates[index]):
                index+=1
            
            dfs(curr,sum,index)

        dfs([], 0, 0)
        return ans