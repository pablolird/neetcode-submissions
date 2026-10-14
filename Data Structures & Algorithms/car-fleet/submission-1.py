class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), reverse=True))

        fleets = 0
        lead_time = 0
        for i, p in enumerate(position):
            time = (target - p) / speed[i]
            if time > lead_time:
                fleets += 1
                lead_time = time

        return fleets