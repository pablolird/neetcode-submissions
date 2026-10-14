class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height)-1]

        p1 = 0
        p2 = len(height)-1

        water = 0

        while p1<p2:
            if (leftMax<rightMax):
                w = leftMax-height[p1]
                p1+=1
                if (leftMax<height[p1]):
                    leftMax = height[p1]
                

            
            else:
                w=rightMax-height[p2]
                p2-=1
                if (rightMax<height[p2]):
                    rightMax = height[p2]
                
            
            if w<0:
                w=0
            water+=w

        return water
            


