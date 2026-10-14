import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        # userId -> list of (time, tweetId), oldest to newest
        self.tweets = {}
        # userId -> set of followees
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        ans = []

        users = self.follows.get(userId, set()) | {userId}

        for uid in users:
            tweetList = self.tweets.get(uid, [])
            if tweetList:
                idx = len(tweetList) - 1
                time, tweetId = tweetList[idx]
                # Negate time so the min-heap pops the newest first
                heapq.heappush(h, (-time, tweetId, uid, idx))

        while h and len(ans) < 10:
            _, tweetId, uid, idx = heapq.heappop(h)
            ans.append(tweetId)
            if idx > 0:
                time, nextId = self.tweets[uid][idx - 1]
                heapq.heappush(h, (-time, nextId, uid, idx - 1))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows.get(followerId, set()).discard(followeeId)