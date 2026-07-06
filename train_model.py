import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier

# Load dataset
data = pd.read_csv("dataset/flood.csv")

# Convert FloodProbability into binary class
# >= 0.5 = Flood (1)
# < 0.5 = No Flood (0)
data["Flood"] = (data["FloodProbability"] >= 0.5).astype(int)

# Features and target
X = data.drop(columns=["FloodProbability", "Flood"])
y = data["Flood"]
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ]),

    "XGBoost": XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )
}

best_model = None
best_accuracy = 0

print("=" * 40)
print("MODEL ACCURACY")
print("=" * 40)

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"{name:20} : {accuracy*100:.2f}%")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save best model
joblib.dump(best_model, "models/flood_model.pkl")
feature_names = X.columns.tolist()
joblib.dump(feature_names, "models/feature_names.pkl")
print("\n" + "=" * 40)
print("Best Model Saved Successfully!")
print(f"Best Accuracy : {best_accuracy*100:.2f}%")
print("=" * 40)