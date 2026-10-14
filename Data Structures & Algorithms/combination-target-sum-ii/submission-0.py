class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(index, nums, currentSum):
            if currentSum == target:
                ans.append(nums.copy())
                return
            if index == len(candidates) or currentSum > target:
                return

            # include candidates[index]
            nums.append(candidates[index])
            dfs(index + 1, nums, currentSum + candidates[index])
            nums.pop()

            # skip candidates[index] AND every copy of that value
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            dfs(next_index, nums, currentSum)

        dfs(0, [], 0)
        return ans