# RentCast AI – Airbnb Price Prediction Dashboard

RentCast AI is a **Machine Learning powered web application** that predicts Airbnb listing prices based on property features such as neighbourhood, room type, number of beds, reviews, rating, and host experience.

The application combines **Machine Learning, Data Analytics, and an interactive dashboard** to estimate competitive Airbnb prices and visualize market insights.

---

# Live Demo

https://rentcast-ai.onrender.com

You can access the deployed application here and test the Airbnb price prediction model directly.

---

# Project Overview

Airbnb hosts often struggle to determine the optimal listing price.  
RentCast AI uses a trained Machine Learning model to estimate competitive prices based on listing characteristics.

The system includes:

• Price prediction interface  
• Monitoring dashboard  
• Dataset analytics panel  
• Interactive charts and visual insights  

The application is built using **Flask for backend APIs and Chart.js for data visualization.**

---

# Features

### Price Prediction
Predict Airbnb listing price based on property details.

### Monitoring Dashboard
Track prediction history and model activity.

### Dataset Analytics
Explore dataset statistics and distribution.

### Interactive Charts
Visualize predictions, trends, and market insights.

### Dark Mode UI
Modern dashboard interface with dark/light theme.

### API Access
Prediction API endpoint for external integration.

---

# Tech Stack

### Backend
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Gunicorn

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js
- FontAwesome

### Machine Learning
- Scikit-learn Pipeline
- Feature preprocessing
- Regression model for price prediction

---

# Project Structure

```
rentcast-ai-airbnb-price-predictor
│
├── app.py
├── requirements.txt
├── runtime.txt
├── render.yaml
├── README.md
│
├── data
│   └── clean_airbnb_data.csv
│
├── models
│   └── airbnb_pipeline.pkl
│
├── logs
│   └── prediction_history.csv
│
├── templates
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│   └── analytics.html
│
└── static
    ├── css
    │   └── style.css
    └── js
        └── script.js
```

---

# Screenshots

### Prediction Interface
Users enter listing details to estimate Airbnb price.

### Prediction Result
Displays predicted price, estimated range, and feature influence.

### Monitoring Dashboard
Tracks prediction history and model activity.

### Dataset Analytics
Visualizes dataset insights and price distribution.

---

# Installation

Clone the repository
git clone https://github.com/Tmmfaris/rentcast-ai-airbnb-price-predictor.git


### Move to project directory


cd rentcast-ai-airbnb-price-predictor


### Install dependencies


pip install -r requirements.txt


### Run the application


python app.py


### Open the application in browser


http://127.0.0.1:5000

---

# API Endpoint

The application provides a REST API for predictions.

### Endpoint
POST /api/predict


### Example Request

---
{
"neighbourhood": "Manhattan",
"property_type": "Apartment",
"room_type": "Entire home/apt",
"zipcode": 10001,
"beds": 2,
"number_of_reviews": 25,
"review_scores_rating": 90,
"host_experience": 3
}
---

### Example Response

---
{
"predicted_price": 145.20
}
---

---

# Machine Learning Pipeline

The model pipeline performs:

1. Feature preprocessing
2. Encoding categorical variables
3. Scaling numerical features
4. Regression model prediction
5. Calibration adjustment for realistic pricing

---

# Future Improvements

• Real-time Airbnb dataset integration  
• Model retraining pipeline  
• Explainable AI using SHAP values  
• Interactive map visualization  
• Deployment using Docker and cloud services  

---

# Author

### Muhammed Faris T M  
MSc Physics  
Data Science & AI Enthusiast

---

# License

This project is for educational and research purposes.
