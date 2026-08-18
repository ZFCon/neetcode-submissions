import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 1. Time goes negative so NEWEST posts sit at the root of the min-heap
        self.time -= 1
        tweet_node = (self.time, tweetId)
        
        # Initialize user if they don't exist yet
        self.users[userId] = self.users.get(userId, dict())
        self.users[userId]["posts"] = self.users[userId].get("posts", [])
        self.users[userId]["feed"] = self.users[userId].get("feed", [])
        self.users[userId]["followers"] = self.users[userId].get("followers", set())
        
        # 2. Save to own posts AND push to own feed
        self.users[userId]["posts"].append(tweet_node)
        heapq.heappush(self.users[userId]["feed"], tweet_node)
            
        # 3. Fan-out: Push to all followers' feeds
        for followerId in self.users[userId]["followers"]:
            self.users[followerId] = self.users.get(followerId, dict())
            self.users[followerId]["feed"] = self.users[followerId].get("feed", [])
            
            heapq.heappush(self.users[followerId]["feed"], tweet_node)

    def getNewsFeed(self, userId: int) -> List[int]:
        self.users[userId] = self.users.get(userId, dict())
        feed = self.users[userId].get("feed", [])
        
        recent_posts = []
        
        # 1. Pop the top 10 newest tweets out of the heap
        while feed and len(recent_posts) < 10:
            recent_posts.append(heapq.heappop(feed))
            
        # 2. Push them immediately back into the heap so they aren't lost
        for post in recent_posts:
            heapq.heappush(feed, post)
            
        # Return just the tweet IDs
        return [tweetId for time, tweetId in recent_posts]

    def follow(self, followerId: int, followeeId: int) -> None:
        # A user cannot follow themselves
        if followerId == followeeId:
            return
            
        self.users[followeeId] = self.users.get(followeeId, dict())
        self.users[followeeId]["followers"] = self.users[followeeId].get("followers", set())
        
        # Only process if they aren't already following
        if followerId not in self.users[followeeId]["followers"]:
            self.users[followeeId]["followers"].add(followerId)
            
            self.users[followerId] = self.users.get(followerId, dict())
            self.users[followerId]["feed"] = self.users[followerId].get("feed", [])
            
            # Retroactively add the followee's past posts to the follower's feed
            followee_posts = self.users[followeeId].get("posts", [])
            for post in followee_posts:
                heapq.heappush(self.users[followerId]["feed"], post)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # A user cannot unfollow themselves
        if followerId == followeeId:
            return
            
        self.users[followeeId] = self.users.get(followeeId, dict())
        self.users[followeeId]["followers"] = self.users[followeeId].get("followers", set())
        self.users[followeeId]["followers"].discard(followerId)
        
        # Remove the unfollowed user's posts from the follower's feed
        followee_posts = set(self.users[followeeId].get("posts", []))
        
        if followerId in self.users and "feed" in self.users[followerId]:
            new_feed = []
            for post in self.users[followerId]["feed"]:
                if post not in followee_posts:
                    new_feed.append(post)
            
            # Replace old feed and re-heapify
            self.users[followerId]["feed"] = new_feed
            heapq.heapify(self.users[followerId]["feed"])