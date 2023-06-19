import re

import requests
from bs4 import BeautifulSoup


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

    # remove any characters in the text that are not alphabets, digits, or spaces.
    if len(result_string) <= 50:
        result_string = re.sub(r"[^a-zA-Z0-9 ]+", "", soup.get_text())

    # Save the paragraphs to a file in a single line
    with open("paragraph.txt", "w", encoding="utf-8") as file:
        file.write(result_string)

    # return the resulting string
    return result_string
