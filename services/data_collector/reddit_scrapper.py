import praw
import time
from services.storage.nosql_storage import NoSQLStorage

class RedditLongPolling:
    def __init__(self, client_id, client_secret, user_agent, subreddit, dynamodb_table):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
        self.subreddit = subreddit
        self.nosql_storage = NoSQLStorage(dynamodb_table)

    def poll_for_new_posts(self):
        for submission in self.reddit.subreddit(self.subreddit).stream.submissions():
            # You can filter posts based on certain criteria, e.g., keywords or upvotes
            self.store_new_post(submission)

    def store_new_post(self, submission):
        # Store Reddit post in NoSQL (DynamoDB)
        item = {
            "id": submission.id,
            "title": submission.title,
            "url": submission.url,
            "created_utc": submission.created_utc,
            "author": submission.author.name if submission.author else "Unknown"
        }
        self.nosql_storage.put_item(item)
        print(f"Stored post: {submission.title}")
