import pickle

from flask import Flask, render_template, request
from flask_cors import CORS
from models import Prediction, db
from scraper import scrape

# Load the saved model
with open("model.pkl", "rb") as file:
    naive_bayes = pickle.load(file)

# Load the saved vectorizer
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# Flask Configs
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
CORS(app)
db.init_app(app)


# Get List of all previous urls
def get_all():
    all_preds = Prediction.query.order_by(Prediction.id.desc()).all()

    preds_list = []
    for pred in all_preds:
        pred_data = {"id": pred.id, "url": pred.url, "Category": pred.prediction}
        preds_list.append(pred_data)

    return preds_list


# Store url in data base
def add_to_history(url, predction):
    db.session.add(
        Prediction(url=url, prediction=predction),
    )
    db.session.commit()


# Controllers


# Home Page
@app.get("/")
def home():
    return render_template("home.html")


# Predict category for an article
@app.route("/predict", methods=["GET", "POST"])
def predicition():
    if request.method == "GET":
        pred_list = get_all()
        return render_template("prediction.html", pred_list=pred_list, flag=0)
    else:
        # Get the text from the request
        req = request.form["url"]

        # Scrape the article
        text = scrape(req)

        # # Vectorize the text
        text_vectorized = vectorizer.transform([text])

        # # Predict the category for the text
        predicted_category = naive_bayes.predict(text_vectorized)
        add_to_history(req, predicted_category[0])

        pred_list = get_all()

        return render_template(
            "prediction.html", category=predicted_category[0], pred_list=pred_list
        )


if __name__ == "__main__":
    app.run()
