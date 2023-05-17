import requests
from bs4 import BeautifulSoup
import re


# URL of the website you want to scrape
# url = "https://timesofindia.indiatimes.com/business/india-business/jio-bp-kicks-off-price-war-with-super-diesel/articleshow/100288620.cms"


def scrape(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <p> tags in the HTML and extract the text
    paragraphs = [
        re.sub(r"[^a-zA-Z0-9 ]+", "", paragraph.get_text())
        for paragraph in soup.find_all("p")
    ]

    result_string = " ".join(paragraphs)

    if len(result_string) <= 50:
        result_string = re.sub(r"[^a-zA-Z0-9 ]+", "", soup.get_text())

    # Save the paragraphs to a file in a single line
    with open("paragraph.txt", "w", encoding="utf-8") as file:
        file.write(result_string)

    # Print the resulting string
    return result_string


# print(scrape(url))
