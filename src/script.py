"""
Reddit User Post Statistics
Retrieve detailed statistics for your Reddit posts
"""

import praw
import config
import csv
from datetime import datetime

def get_user_posts_detailed(limit=10):
    """
    Get detailed statistics for the user's recent posts.
    
    Args:
        limit (int): Number of recent posts to retrieve (default: 10)
    
    Returns:
        list of dict: Each dict contains detailed post statistics
    """
    # Validate configuration
    required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET',
                     'REDDIT_USERNAME', 'REDDIT_PASSWORD']
    missing_vars = [var for var in required_vars if not hasattr(config, var)]
    if missing_vars:
        print("❌ Missing configuration variables:")
        for var in missing_vars:
            print(f"   - {var}")
        return []

    try:
        # Connect to Reddit
        reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            username=config.REDDIT_USERNAME,
            password=config.REDDIT_PASSWORD,
            user_agent=getattr(config, 'REDDIT_USER_AGENT', 'RedditStatsGetter/1.0')
        )

        print(f"🔍 Fetching posts for u/{config.REDDIT_USERNAME}...\n")
        user = reddit.user.me()
        posts_stats = []

        for submission in user.submissions.new(limit=limit):
            # Calculate downvotes
            downvotes = int(submission.ups * (1 - submission.upvote_ratio) / submission.upvote_ratio) if submission.upvote_ratio > 0 else 0
            
            stats = {
                "id": submission.id,
                "title": submission.title,
                "subreddit": submission.subreddit.display_name,
                "url": submission.url,
                "permalink": f"https://reddit.com{submission.permalink}",
                "created_utc": datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                "upvotes": submission.ups,
                "downvotes": downvotes,
                "score": submission.score,
                "upvote_ratio": submission.upvote_ratio,
                "num_comments": submission.num_comments,
                "total_awards": submission.total_awards_received,
                "gilded": submission.gilded,
                "is_self": submission.is_self,
                "spoiler": submission.spoiler,
                "over_18": submission.over_18,
                "stickied": submission.stickied,
                "locked": submission.locked,
            }
            posts_stats.append(stats)

        return posts_stats

    except Exception as e:
        print(f"❌ Error fetching posts: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

def display_posts_stats(posts_stats):
    """
    Display the detailed statistics in a readable table format.
    """
    if not posts_stats:
        print("No posts to display.")
        return

    print(f"\n{'='*80}")
    print(f"📊 Reddit Posts Statistics - {len(posts_stats)} posts")
    print(f"{'='*80}\n")

    for i, post in enumerate(posts_stats, 1):
        print(f"Post #{i}: {post['title']}")
        print(f"Subreddit: {post['subreddit']}")
        print(f"URL: {post['permalink']}")
        print(f"Created UTC: {post['created_utc']}")
        print(f"👍 Upvotes: {post['upvotes']} | 👎 Downvotes: {post['downvotes']} | Score: {post['score']} | Ratio: {post['upvote_ratio']}")
        print(f"💬 Comments: {post['num_comments']} | Awards: {post['total_awards']} | Gilded: {post['gilded']}")
        print(f"Self Post: {post['is_self']} | NSFW: {post['over_18']} | Spoiler: {post['spoiler']} | Stickied: {post['stickied']} | Locked: {post['locked']}")
        print(f"{'-'*80}")

    # Totals
    total_upvotes = sum(post['upvotes'] for post in posts_stats)
    total_downvotes = sum(post['downvotes'] for post in posts_stats)
    total_comments = sum(post['num_comments'] for post in posts_stats)
    total_awards = sum(post['total_awards'] for post in posts_stats)
    print(f"\n{'='*80}")
    print(f"TOTALS - Upvotes: {total_upvotes} | Downvotes: {total_downvotes} | Comments: {total_comments} | Awards: {total_awards}")
    print(f"{'='*80}\n")

def export_to_csv(posts_stats, filename="reddit_posts_stats.csv"):
    """
    Export the post statistics to a CSV file.
    """
    if not posts_stats:
        print("No posts to export.")
        return

    keys = posts_stats[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(posts_stats)

    print(f"✅ Data exported to {filename}\n")


