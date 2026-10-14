class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), reverse=True))

        ans = 0
        for i, p in enumerate(position):
            if (i==0):
                pointer = i
            elif ((target-position[pointer])/speed[pointer])<((target-position[i])/speed[i]):
                ans+=1
                pointer = i
        

        return ans+1

        