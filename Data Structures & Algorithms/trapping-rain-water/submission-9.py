class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)

        for i, h in enumerate(height):
            if i==0:
                leftMax[i]=h
                continue
            
            if leftMax[i-1] < h:
                leftMax[i] = h
            else:
                leftMax[i] = leftMax[i-1]

        for i in reversed(range(len(height))):
            if i==len(height)-1:
                rightMax[i]=height[i]
                continue
            
            if rightMax[i+1] < height[i]:
                rightMax[i] = height[i]
            else:
                rightMax[i] = rightMax[i+1]
        
        water = 0

        for i in range(len(height)):
            w = min(leftMax[i], rightMax[i])-height[i]
            if w<0:
                continue
            water+=w
        
        return water
                