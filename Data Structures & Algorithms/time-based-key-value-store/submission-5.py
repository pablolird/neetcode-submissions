class TimeMap:
    map = {}

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
        else:
            self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            l = 0
            r = len(self.map[key])-1

            while (l<r):
                mid = (l+r+1)//2

                if (self.map[key][mid][0]==timestamp):
                    return self.map[key][mid][1]
                elif (self.map[key][mid][0]<timestamp):
                    l = mid
                else:
                    r = mid-1
            
            if (self.map[key][l][0]>timestamp):
                return ""
            return self.map[key][l][1]
