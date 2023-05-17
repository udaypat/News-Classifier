from flask import Flask, request, jsonify
from scraper import scrape
import pickle

import os

print(os.getcwd())


# Load the saved model and vectorizer
with open("model.pkl", "rb") as file:
    naive_bayes = pickle.load(file)

with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


app = Flask(__name__)


@app.get("/")
def home():
    return jsonify("home")


@app.post("/predict")
def predict():
    # Get the text from the request
    req = request.get_json()
    text = scrape(req["url"])

    # Vectorize the text
    text_vectorized = vectorizer.transform([text])

    # Predict the category for the text
    predicted_category = naive_bayes.predict(text_vectorized)

    # Return the predicted category as JSON response
    response = {"predicted_category": predicted_category[0]}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
