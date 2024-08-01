import praw

def scrape_descriptions(client_id, client_secret, user_agent, subreddit_name, num_posts, time_filter='all'):
    """
    Scrape descriptions from a subreddit.

    Parameters:
    - client_id: str, Reddit API client ID
    - client_secret: str, Reddit API client secret
    - user_agent: str, Reddit API user agent
    - subreddit_name: str, the name of the subreddit to scrape
    - num_posts: int, the number of posts to scrape
    - time_filter: str, the time filter for scraping posts ('all', 'day', 'week', 'month', 'year')

    Returns:
    - descriptions: list of str, the scraped post descriptions
    """
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    descriptions = []
    
    for submission in subreddit.top(time_filter=time_filter, limit=num_posts):
        descriptions.append(submission.selftext)
    
    return descriptions

def save_descriptions_to_file(descriptions, output_file):
    """
    Save the descriptions to a file.

    Parameters:
    - descriptions: list of str, the post descriptions
    - output_file: str, the path to the output file
    """
    with open(output_file, 'w') as file:
        for desc in descriptions:
            file.write(desc + '\n\n')

# Example usage
if __name__ == '__main__':
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    user_agent = 'YOUR_USER_AGENT'
    subreddit_name = 'example_subreddit'
    num_posts = 10
    time_filter = 'week'
    output_file = 'descriptions.txt'
    
    descriptions = scrape_descriptions(client_id, client_secret, user_agent, subreddit_name, num_posts, time_filter)
    save_descriptions_to_file(descriptions, output_file)
    print(f"Descriptions scraped and saved to {output_file}")
