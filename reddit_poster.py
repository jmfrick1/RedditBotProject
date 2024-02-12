# reddit_poster.py
from praw_setup import create_reddit_instance
from content_generator import generate_post_content, load_descriptions
from image_handler import select_random_image
# Assume a hypothetical function `upload_image_to_imgur` exists that uploads an image and returns a URL
from imgur_uploader import upload_image_to_imgur  

def post_to_reddit(subreddit_name, descriptions_file, image_dir):
    # Initialize Reddit instance
    reddit = create_reddit_instance()

    # Load descriptions and generate post content
    descriptions = load_descriptions(descriptions_file)
    title, body = generate_post_content(descriptions)

    # Select a random image and upload it to get a URL
    image_path = select_random_image(image_dir)
    image_url = upload_image_to_imgur(image_path) if image_path else None

    # Include the image URL in the post body if available
    if image_url:
        body += f"\n\n![Image]({image_url})"

    # Submit the post
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.submit(title, selftext=body)

# Example usage
if __name__ == '__main__':
    subreddit_name = 'test'  # Change this to the target subreddit
    descriptions_file = 'descriptions.txt'  # Path to your descriptions file
    image_dir = 'path/to/your/image/directory'  # Update this path to your image directory
    post_to_reddit(subreddit_name, descriptions_file, image_dir)
