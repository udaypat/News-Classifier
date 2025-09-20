# Table of Contents

- [Introduction](#news-article-classifier-app)
- [Installation](#installation)
  - [Using docker 🐋](#using-docker)
  - [Manual Install](#manual-install)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Hosting on Linux with Nginx](#hosting-on-linux-with-nginx)

# News Article Classifier App

This is a web application that classifies news articles into different categories such as sports, business, politics, tech, and entertainment. The app is built using Flask and Jinja and runs using Gunicorn. It utilizes a Scraper service to scrape articles using Beautiful Soup and a machine learning model built with scikit-learn to perform the classification.

## Installation

### Using docker

1. Build the container:

   ```
   docker build https://github.com/udaypat/News-Classifier.git -t news-classifier
   ```

2. Run the container:

   ```
   docker run -p 8000:8000 news-classifier
   ```

### Manual Install

To install it manually and run the News Article Classifier App on your local machine, follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/udaypat/News-Classifier.git
   ```

2. Navigate to the project directory:

   ```
   cd server
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. To train the model again:
   ```
   cd predictor
   jupyter nbconvert --execute classify.ipyb
   ```
5. To start the Flask application:

   ```
   cd app
   gunicorn main:app
   ```

6. Access the app in your web browser at `http://localhost:5000`.

### Lock Dependencies

uv pip compile --universal requirements.in -o requirements.txt

## Project Structure

1. The ML model was trained on bbc-news dataset. - https://storage.googleapis.com/dataset-uploader/bbc/bbc-text.csv

2. After removing stopwords the accurcay was measured of different classifiers.

3. Trained model was dumped using pickle and use by a flask endpoint to make prediction.

4. Scraping of data was done using BeautifulSoup.
   All <p> tags were extrated, If there was no <p> tags Plain text was extracted.

5. On basis of that new predicitons were made and stored in the Sqlite Database.

## Usage

1. Open the News Article Classifier App in your web browser.

2. On the homepage, you will find a button which will redirect you where can enter the URL of a news article.

3. Enter the URL of the article you want to classify and click the "Classify" button.

4. The app will scrape the article using the Scraper service and pass it to the machine learning model for classification.

5. Once the classification is complete, the app will display the predicted category of the article on the result page.

6. App will store previous results in a database and will show a list after prediction.

## Hosting on Linux with Nginx

This News Article Classifier App is designed to be hosted on Linux. To host the app on Linux, follow these steps:

1. Create a Droplet on DigitalOcean with your preferred specifications and operating system or use your own system.

2. SSH into your Droplet.

   ```
   ssh root@ip
   ```

3. Run

   ```
   sudo apt update
   sudo apt install python3-pip
   ```

4. Clone the repository onto your Droplet:

   ```
   git clone https://github.com/udaypat/News-Classifier.git
   ```

5. Navigate to the project directory:

   ```
   cd
   ```

6. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

7. Install Gunicorn if not already installed:

   ```
   pip install gunicorn
   ```

8. Start the Gunicorn server:

   ```
   gunicorn main:app
   ```

9. Install Nginx

   ```
    sudo apt install nginx
    sudo systemctl enable nginx
    sudo systemctl start nginx
   ```

10. Access the app in your web browser using the IP address or domain name of your DigitalOcean Droplet.
