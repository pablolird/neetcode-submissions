class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        # it might simplify the logic using float('-inf') and float('inf')
        if (self.h1):
            if not self.h2:
                if (num>-self.h1[0]):
                    self.h2 = [num]
                else:
                    heapq.heappush(self.h1, -num)
            elif (-self.h1[0]<=num<=self.h2[0]):
                if (len(self.h2)>len(self.h1)):
                    heapq.heappush(self.h1, -num)
                else:
                    heapq.heappush(self.h2, num)
            elif (num<-self.h1[0]):
                heapq.heappush(self.h1, -num)
            else:
                heapq.heappush(self.h2, num)
        else:
            self.h1 = [-num]
        
        if (abs(len(self.h1)-len(self.h2))>1):
            if (len(self.h1)>len(self.h2)):
                v = heapq.heappop(self.h1)
                heapq.heappush(self.h2, -v)
            else:
                v = heapq.heappop(self.h2)
                heapq.heappush(self.h1, -v)

    def findMedian(self) -> float:
        if ((len(self.h1)+len(self.h2))%2==0):
            return (-self.h1[0]+self.h2[0])/2
        else:
            if (len(self.h2)>len(self.h1)):
                return self.h2[0]
            else:
                return -self.h1[0]
        