import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Send HTTP request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all headline tags (BBC uses h2 and h3 for headlines)
    headlines = soup.find_all(["h2", "h3"])
    
    # Open a text file to save headlines
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:  # Avoid empty lines
                print(text)
                file.write(text + "\n")
    
    print("\nHeadlines saved to headlines.txt")

else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
