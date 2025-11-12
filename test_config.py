"""
Test Reddit API Configuration
Run this script to verify your Reddit credentials are correct.
"""
import praw
import config

def test_reddit_connection():
    """Test the Reddit API connection and credentials."""
    print("=== Testing Reddit Configuration ===\n")
    
    # Check config variables
    print("1. Checking configuration variables...")
    required = {
        'REDDIT_CLIENT_ID': getattr(config, 'REDDIT_CLIENT_ID', None),
        'REDDIT_CLIENT_SECRET': getattr(config, 'REDDIT_CLIENT_SECRET', None),
        'REDDIT_USERNAME': getattr(config, 'REDDIT_USERNAME', None),
        'REDDIT_PASSWORD': getattr(config, 'REDDIT_PASSWORD', None),
    }
    
    for key, value in required.items():
        if not value:
            print(f"   ❌ {key} is missing")
        else:
            # Show partial value for security
            if 'SECRET' in key or 'PASSWORD' in key:
                display = f"{value[:4]}...{value[-4:]}" if len(value) > 8 else "****"
            else:
                display = value
            print(f"   ✓ {key}: {display}")
    
    print("\n2. Testing Reddit API connection...")
    try:
        reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            username=config.REDDIT_USERNAME,
            password=config.REDDIT_PASSWORD,
            user_agent=getattr(config, 'REDDIT_USER_AGENT', 'RedditPublisher/1.0')
        )
        
        # Test authentication
        print(f"   ✓ Attempting authentication...")
        user = reddit.user.me()
        print(f"   ✓ Successfully authenticated as: {user.name}")
        print(f"   ✓ Account karma: {user.link_karma + user.comment_karma}")
        
        return True
        
    except praw.exceptions.ResponseException as e:
        print(f"\n   ❌ Authentication failed!")
        print(f"   Error: {e}")
        print("\n   Common causes:")
        print("   - Incorrect username or password")
        print("   - Incorrect client_id or client_secret")
        print("   - 2FA enabled (need to use app password)")
        return False
        
    except Exception as e:
        print(f"\n   ❌ Connection error: {e}")
        return False

if __name__ == "__main__":
    test_reddit_connection()