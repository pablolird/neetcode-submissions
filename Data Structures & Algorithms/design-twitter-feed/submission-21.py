class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if (userId in self.tweets):
            self.tweets[userId].append((self.time, tweetId))
            return
        self.tweets[userId] = [(self.time, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        userList = self.follows.get(userId, set())
        userList.add(userId)
        # userList contains a list of userId's which will
        # be used for creating the heap
        ans = []
        heap = []

        for userId in userList:
            tweets = self.tweets.get(userId, [])

            if tweets:
                i = len(tweets)-1
                # [0][0] => -time
                # [0][1] => tweetId
                # [2] => nextId
                # [3] => userId
                heap.append((-tweets[i][0], tweets[i][1], i, userId))
        
        heapq.heapify(heap)

        while (heap and len(ans)<10):
            _, tweetId, i, userId = heapq.heappop(heap)
            ans.append(tweetId)
            if (i>0):
                tweets = self.tweets[userId]
                heapq.heappush(heap, (-tweets[i-1][0], tweets[i-1][1], i-1, userId))
            
        return ans


        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
            return
        self.follows[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
            return
