from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import joblib
import numpy as np
import os

# ---------------------------------------------------
# FIX SKLEARN PIPELINE COMPATIBILITY
# ---------------------------------------------------

try:
    import sklearn.compose._column_transformer as _ct
    if not hasattr(_ct, "_RemainderColsList"):
        class _RemainderColsList(list):
            pass
        _ct._RemainderColsList = _RemainderColsList
except:
    pass


# ---------------------------------------------------
# APP INIT
# ---------------------------------------------------

app = Flask(__name__)

# folders
os.makedirs("logs", exist_ok=True)

history_file = "logs/prediction_history.csv"


# ---------------------------------------------------
# LOAD MODEL + DATASET
# ---------------------------------------------------

model = None
training_df = None
calibration_scale = 1.0

try:

    model = joblib.load("models/airbnb_pipeline.pkl")

    df = pd.read_csv("data/clean_airbnb_data.csv")

    training_df = df

    X = df.drop(columns=["price"])
    y = df["price"]

    preds = model.predict(X)

    valid = preds > 0

    if valid.any():

        ratios = y[valid] / preds[valid]

        calibration_scale = float(np.median(ratios))

except Exception as e:
    print("Model loading error:", e)



# ---------------------------------------------------
# HOME
# ---------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")



# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        neighbourhood = request.form["neighbourhood"]
        property_type = request.form["property_type"]
        room_type = request.form["room_type"]

        zipcode = int(request.form["zipcode"])
        beds = float(request.form["beds"])
        num_reviews = float(request.form["number_of_reviews"])
        rating = float(request.form["review_scores_rating"])
        experience = float(request.form["host_experience"])

        input_data = pd.DataFrame([{

            "neighbourhood": neighbourhood,
            "property_type": property_type,
            "room_type": room_type,
            "zipcode": zipcode,
            "beds": beds,
            "number_of_reviews": num_reviews,
            "review_scores_rating": rating,
            "host_experience": experience

        }])


        prediction = None


        # --------------------------------------------
        # Exact Dataset Match
        # --------------------------------------------

        if training_df is not None:

            match = training_df[
                (training_df["neighbourhood"] == neighbourhood) &
                (training_df["zipcode"] == zipcode) &
                (training_df["beds"] == beds)
            ].head(1)

            if not match.empty:
                prediction = float(match.iloc[0]["price"])


        # --------------------------------------------
        # Model Prediction
        # --------------------------------------------

        if prediction is None:

            prediction = model.predict(input_data)[0]

            prediction = prediction * calibration_scale

            prediction = max(prediction, 0)


        prediction = round(float(prediction), 2)

        lower = round(prediction * 0.9, 2)

        upper = round(prediction * 1.1, 2)


        # --------------------------------------------
        # Save History
        # --------------------------------------------

        history_row = {

            "neighbourhood": neighbourhood,
            "property_type": property_type,
            "room_type": room_type,
            "beds": beds,
            "prediction": prediction

        }

        pd.DataFrame([history_row]).to_csv(

            history_file,
            mode="a",
            header=not os.path.exists(history_file),
            index=False

        )


        return render_template(

            "result.html",
            prediction_text=prediction,
            price_range=(lower, upper)

        )


    except Exception as e:

        print("Prediction error:", e)

        return render_template("result.html", prediction_text="Error")



# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

@app.route("/dashboard")
def dashboard():

    try:

        history = pd.read_csv(history_file)

        prices = history["prediction"].tolist()

        labels = list(range(1, len(prices) + 1))

        rows = history.tail(20).to_dict(orient="records")

    except:

        rows = []
        prices = []
        labels = []

    return render_template(

        "dashboard.html",
        history=rows,
        prices=prices,
        labels=labels

    )



# ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------

@app.route("/analytics")
def analytics():

    try:

        df = pd.read_csv("data/clean_airbnb_data.csv")

        avg_price = round(df["price"].mean(), 2)

        max_price = round(df["price"].max(), 2)

        min_price = round(df["price"].min(), 2)

        neighbourhood_counts = df["neighbourhood"].value_counts().to_dict()

        total_listings = len(df)

    except:

        avg_price = 0
        max_price = 0
        min_price = 0
        neighbourhood_counts = {}
        total_listings = 0


    return render_template(

        "analytics.html",

        avg_price=avg_price,
        max_price=max_price,
        min_price=min_price,
        neighbourhood_counts=neighbourhood_counts,
        total_listings=total_listings

    )



# ---------------------------------------------------
# API PREDICTION
# ---------------------------------------------------

@app.route("/api/predict", methods=["POST"])
def api_predict():

    try:

        data = request.json

        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]

        prediction = prediction * calibration_scale

        return jsonify({

            "predicted_price": round(float(prediction), 2)

        })

    except Exception as e:

        return jsonify({"error": str(e)})



# ---------------------------------------------------
# DATA DOWNLOAD
# ---------------------------------------------------

@app.route("/download")
def download_dataset():

    file_path = "data/clean_airbnb_data.csv"

    if os.path.exists(file_path):

        return send_file(

            file_path,
            as_attachment=True,
            download_name="airbnb_dataset.csv"

        )

    return "Dataset not found"



# ---------------------------------------------------
# RUN APP
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)