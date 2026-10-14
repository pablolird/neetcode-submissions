class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0

        for i, p in enumerate(heights):
            b = i
            while (stack and stack[-1][1] > heights[i]):
                x = stack.pop()
                b = x[0]
                max_height = max(max_height, (i-x[0])*x[1])
            stack.append([b, heights[i]])

        while (stack):
            x = stack.pop()
            max_height = max(max_height, (len(heights)-x[0])*x[1])
        
        return max_height