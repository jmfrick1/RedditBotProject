# description_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_descriptions(url, output_file):
    # jmf's Description Scraper
    # Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find elements containing descriptions (adjust this based on actual HTML structure) 
    ##'p' might not work as 'p' is just an example and stands for paragraph tags in HTML.
    descriptions = soup.find_all('p')  # Example: find all paragraph tags

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        for desc in descriptions:
            file.write(desc.text + '\n\n')  # Write each description to the file

# Example usage
if __name__ == '__main__':
    scrape_descriptions('http://example.com', 'descriptions.txt')
    print("Descriptions scraped and saved to descriptions.txt")
