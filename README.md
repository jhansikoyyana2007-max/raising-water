# 🌊 Flood Prediction System using Machine Learning

## Overview

Floods are among the most devastating natural disasters, causing significant loss of life, property damage, and displacement of communities every year. Timely and accurate flood prediction plays a vital role in minimizing these impacts by enabling authorities to take preventive measures and issue early warnings.

This project presents a **Machine Learning-based Flood Prediction System** that predicts the likelihood of flood occurrence using historical environmental and meteorological data. The system compares multiple machine learning algorithms, including **Decision Tree**, **Random Forest**, **K-Nearest Neighbours (KNN)**, and **XGBoost**, to identify the most effective prediction model.

The trained model is integrated into a **Flask web application**, allowing users to enter flood-related parameters and instantly receive a flood risk prediction through a user-friendly interface. The application is designed to be scalable and can be deployed on **IBM Cloud** for remote accessibility.

---

## Features

* Machine Learning-based flood prediction
* Comparison of multiple classification algorithms
* Automatic selection of the best-performing model
* Interactive Flask web application
* Professional Bootstrap-based user interface
* Real-time flood risk prediction
* Model persistence using Joblib
* IBM Cloud deployment ready

---

## Technologies Used

### Programming Language

* Python 3.x

### Machine Learning Libraries

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib

### Web Framework

* Flask

### Frontend

* HTML5
* CSS3
* Bootstrap 5

---

## Machine Learning Models

The following classification algorithms were implemented and evaluated:

* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbours (KNN)
* XGBoost Classifier

The best-performing model is automatically selected and saved for use in the web application.

---

## Project Structure

```text
flood_prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── flood.csv
│
├── models/
│   ├── flood_model.pkl
│   └── feature_names.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── venv/
```

---

## Dataset

The dataset contains environmental and flood-related parameters such as:

* Monsoon Intensity
* Topography Drainage
* River Management
* Deforestation
* Urbanization
* Climate Change
* Dams Quality
* Siltation
* Agricultural Practices
* Encroachments
* Disaster Preparedness
* Drainage Systems
* Coastal Vulnerability
* Landslides
* Watersheds
* Deteriorating Infrastructure
* Population Score
* Wetland Loss
* Inadequate Planning
* Political Factors

Target Variable:

* Flood Probability (converted into binary flood classification during training)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/flood-prediction-system.git
```

Navigate to the project directory:

```bash
cd flood-prediction-system
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run the following command:

```bash
python train_model.py
```

This will:

* Load the dataset
* Train all machine learning models
* Compare their performance
* Save the best-performing model
* Save the feature names

Saved files:

* `models/flood_model.pkl`
* `models/feature_names.pkl`

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Enter the required input parameters and click **Predict Flood Risk** to obtain the prediction.

---

## Application Workflow

1. User enters environmental parameters.
2. Flask receives the input data.
3. The trained machine learning model processes the input.
4. The application predicts the flood risk.
5. The result and confidence score are displayed to the user.

---

## Use Case Scenarios

### Scenario 1 – Early Flood Warning

A meteorologist enters current environmental conditions for a flood-prone district. The system predicts a high flood risk, enabling authorities to issue early evacuation warnings.

### Scenario 2 – Disaster Response

A disaster management officer monitors multiple regions by entering regional environmental data. The application helps prioritize emergency response and resource allocation.

### Scenario 3 – Model Validation

Government agencies evaluate the prediction model using historical flood records to assess its reliability before operational deployment.

---

## Future Enhancements

* Integration with live weather APIs
* GIS and interactive map visualization
* SMS and email alert notifications
* Real-time rainfall monitoring
* IoT sensor integration
* IBM Cloud deployment
* Mobile application support

---

## Author

**Name:** *Your Name*

**Institution:** *Your College Name*

**Department:** Computer Science / Information Technology

**Academic Year:** 2025–2026

---

## License

This project is developed for educational and academic purposes.
