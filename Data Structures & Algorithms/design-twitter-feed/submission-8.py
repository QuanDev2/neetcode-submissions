"""
linked list to store tweets (timestamp and tweetId)
Need a global timestamp counter
tweetsMap { user -> [TweetNode] }
followMap { user -> set_of_followed_ids }
"""

class TweetNode:
    def __init__(self, tweetId = 0, timestamp = 0):
        self.next = None
        self.tweetId = tweetId
        self.timestamp = timestamp

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.followMap = defaultdict(set)
        self.tweetsMap = defaultdict(lambda: None)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        tweet = TweetNode(tweetId, self.timestamp)
        tweet.next = self.tweetsMap[userId]
        self.tweetsMap[userId] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = list(self.followMap[userId])
        followees = self.followMap[userId] | {userId}
        maxHeap = []

        for fid in followees:
            head = self.tweetsMap[fid]
            if head:
                heapq.heappush(maxHeap, (-head.timestamp, fid, head))

        res = []
        while len(res) < 10 and maxHeap:
            _, heapUserId, tweetNode = heapq.heappop(maxHeap)
            if tweetNode:
                res.append(tweetNode.tweetId)
                if tweetNode.next:
                    heapq.heappush(maxHeap, (-tweetNode.next.timestamp, heapUserId, tweetNode.next))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
