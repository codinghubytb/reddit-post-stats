from src.script import get_user_posts_detailed, display_posts_stats, export_to_csv

def main():
    print("=== Reddit Posts Detailed Statistics ===\n")
    
    posts_stats = get_user_posts_detailed(limit=10)
    if posts_stats:
        display_posts_stats(posts_stats)
        export_to_csv(posts_stats)

if __name__ == "__main__":
    main()