# Reddit User Post Statistics

Retrieve and analyze detailed statistics for your Reddit posts with this Python tool.

## 📋 Features

- Fetch detailed statistics for your recent Reddit posts
- Display comprehensive metrics including upvotes, downvotes, comments, awards
- Export data to CSV format for further analysis
- Easy configuration with environment variables

## 📊 Statistics Tracked

- Post ID, title, subreddit
- URLs (post URL and permalink)
- Creation date and time (UTC)
- Upvotes, downvotes, score, upvote ratio
- Number of comments
- Awards received
- Post metadata (self post, NSFW, spoiler, stickied, locked)

## 🚀 Installation

### 1. Clone or download this repository

```bash
git clone https://github.com/codinghubytb/reddit-post-stats
cd reddit-post-stats
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Reddit API credentials

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Fill in the details:
   - **name**: Choose any name (e.g., "Post Statistics Tool")
   - **App type**: Select "script"
   - **description**: Optional
   - **about url**: Optional
   - **redirect uri**: Use `http://localhost:8080`
4. Click "Create app"
5. Note your **client_id** (under the app name) and **client_secret**

### 4. Configure your credentials

Copy the example configuration file:

```bash
cp config.example.py config.py
```

Edit `config.py` with your Reddit credentials:

```python
REDDIT_CLIENT_ID = "your_client_id_here"
REDDIT_CLIENT_SECRET = "your_client_secret_here"
REDDIT_USERNAME = "your_reddit_username"
REDDIT_PASSWORD = "your_reddit_password"
REDDIT_USER_AGENT = "RedditStatsGetter/1.0"
```

### 5. Test your configuration

```bash
python test_config.py
```

If everything is configured correctly, you should see:
```
✅ Configuration is valid!
✅ Successfully connected to Reddit API
✅ Authenticated as: your_username
```

## 📖 Usage

Run the main script:

```bash
python main.py
```

By default, it fetches statistics for your 10 most recent posts. To change the number of posts:

```python
# In main.py, modify the limit parameter
posts_stats = get_user_posts_detailed(limit=25)  # Fetch 25 posts
```

## 📂 Output

The script generates:
1. **Console output**: Formatted display of all post statistics
2. **CSV file**: `reddit_posts_stats.csv` with all data for spreadsheet analysis

### Sample Console Output

```
================================================================================
📊 Reddit Posts Statistics - 10 posts
================================================================================

Post #1: My Amazing Post Title
Subreddit: python
URL: https://reddit.com/r/python/comments/abc123/my_amazing_post_title
Created UTC: 2024-11-10 14:30:00
👍 Upvotes: 1250 | 👎 Downvotes: 45 | Score: 1205 | Ratio: 0.965
💬 Comments: 87 | Awards: 3 | Gilded: 1
Self Post: True | NSFW: False | Spoiler: False | Stickied: False | Locked: False
--------------------------------------------------------------------------------
```

## 📁 Project Structure

```
reddit-post-statistics/
│
├── src/
│   └── script.py              # Main script with all functions
├── main.py                    # Entry point
├── config.py                  # Your credentials (DO NOT COMMIT)
├── config.example.py          # Configuration template
├── test_config.py             # Configuration validator
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .gitignore                # Git ignore file
```

## ⚠️ Security Notes

- **Never commit `config.py`** to version control
- Keep your Reddit credentials secure
- The `.gitignore` file is configured to exclude `config.py`
- Consider using environment variables for production use

## 🛠️ Troubleshooting

### "Missing configuration variables" error
- Make sure you've created `config.py` from `config.example.py`
- Verify all required variables are set in `config.py`

### "Invalid credentials" error
- Double-check your Reddit API credentials
- Ensure your Reddit account password is correct
- Verify your app is set as "script" type

### "Too Many Requests" error
- Reddit API has rate limits
- Wait a few minutes before trying again
- Consider reducing the number of posts fetched

## 📝 Requirements

See `requirements.txt` for all dependencies. Main requirement:
- `praw` (Python Reddit API Wrapper)

## 🔗 Resources

- [PRAW Documentation](https://praw.readthedocs.io/)
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Reddit Apps Page](https://www.reddit.com/prefs/apps)

---

**Happy analyzing! 📊**