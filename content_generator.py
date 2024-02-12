# content_generator.py
import random

def load_descriptions(file_path):
    # jmf's Description Loader
    ## Load descriptions from the file into a list 
    ### Adjust the splitting logic if your file uses a different format.
    with open(file_path, 'r') as file:
        descriptions = file.read().strip().split('\n\n')
    return descriptions

def generate_post_content(descriptions):
    # jmf's Content Generator
    # Select a random description as the post body
    body = random.choice(descriptions)
    # Generate a title for the post (this is a simple example, you may want to customize this)
    title = "Interesting Fact" if "fact" in body.lower() else "Thought-Provoking Idea"
    return title, body

# Example usage
if __name__ == '__main__':
    descriptions_path = 'descriptions.txt'  # Path to your descriptions file
    descriptions = load_descriptions(descriptions_path)
    title, body = generate_post_content(descriptions)
    print(f"Title: {title}\nBody: {body}")
