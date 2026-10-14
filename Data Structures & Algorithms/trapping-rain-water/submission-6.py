class Solution:
    def trap(self, height):
        pillars = [0]*(len(height))

        i = 0
        while height[i]==0 and i<len(height)-1:
            i+=1

        pillars[i] = 'X'
        max = height[i]

        for x in range(i+1, len(height)):
            if height[x]>=max:
                pillars[x]='X'
                max = height[x]
                continue
            
            pillars[x] = max - height[x]


        i = len(height)-1
        while i >=0 and height[i]==0:
            pillars[i]=0
            i-=1

        if i<=0:
            return 0

        if pillars[i]!='X':
                
            pillars[i] = 'X'
            max = height[i]

            x = i-1
            while (pillars[x]!="X"):        
                if height[x]>=max:
                    pillars[x]='X'
                    max = height[x]
                    x-=1
                    continue
                
                pillars[x] = max - height[x]
                x-=1

        water = 0

        for n in pillars:
            if n=="X":
                continue
            water+=n

        return water
