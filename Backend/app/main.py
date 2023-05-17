from flask import Flask, request, jsonify
from scraper import scrape
import pickle
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

model_path = r"C:\Users\nitro\Documents\IIC\KYRO Assignment\Backend\app\model.pkl"

# Load the saved model and vectorizer
with open(model_path, "rb") as file:
    naive_bayes = pickle.load(file)

vector_path = r"C:\Users\nitro\Documents\IIC\KYRO Assignment\Backend\app\vectorizer.pkl"

with open(vector_path, "rb") as file:
    vectorizer = pickle.load(file)

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"

CORS(app)
# SQLite database file path
db.init_app(app)


class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    prediction = db.Column(db.String(200))


@app.get("/history")
def get_all():
    all_preds = Prediction.query.all()

    preds_list = []
    for pred in all_preds:
        pred_data = {"id": pred.id, "url": pred.url, "Category": pred.prediction}
        preds_list.append(pred_data)
    return jsonify(preds_list)


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

    add_to_history(req["url"], predicted_category[0])

    return jsonify(response)


def add_to_history(url, predction):
    db.session.add(
        Prediction(url=url, prediction=predction),
    )
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
