import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# --------------------------
# Load Dataset
# --------------------------

df = pd.read_csv("career_dataset.csv")

# --------------------------
# Features
# --------------------------

X = df[[
    "O_score",
    "C_score",
    "E_score",
    "A_score",
    "N_score",
    "Numerical Aptitude",
    "Spatial Aptitude",
    "Perceptual Aptitude",
    "Abstract Reasoning",
    "Verbal Reasoning"
]]

# --------------------------
# Target
# --------------------------

y = df["Career"]

# --------------------------
# Encode Labels
# --------------------------

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

joblib.dump(label_encoder, "label_encoder.pkl")

# --------------------------
# Scale Features
# --------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "scaler.pkl")

# --------------------------
# Cross Validation
# --------------------------

cv = StratifiedKFold(
    n_splits=3,
    shuffle=True,
    random_state=42
)

# --------------------------
# Models
# --------------------------

models = {

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            random_state=42
        ),

    "Gradient Boost":
        GradientBoostingClassifier(
            random_state=42
        )
}

scores = {}

print("="*60)
print("MODEL COMPARISON")
print("="*60)

for name, model in models.items():

    pipeline = Pipeline([

        ("model", model)

    ])

    accuracy = cross_val_score(

        pipeline,

        X_scaled,

        y_encoded,

        cv=cv,

        scoring="accuracy"

    )

    mean_accuracy = accuracy.mean()

    scores[name] = mean_accuracy

    print(f"{name:<20} {mean_accuracy:.4f}")

print()

# --------------------------
# Best Model
# --------------------------

best_model_name = max(

    scores,

    key=scores.get

)

best_model = models[best_model_name]

print("Best Model :", best_model_name)

print("Accuracy   :", round(scores[best_model_name]*100,2),"%")

# --------------------------
# Train Best Model
# --------------------------

best_model.fit(

    X_scaled,

    y_encoded

)

# --------------------------
# Save Model
# --------------------------

joblib.dump(

    best_model,

    "career_model.pkl"

)

print("\nModel Saved Successfully!")

# --------------------------
# Prediction
# --------------------------

prediction = best_model.predict(

    X_scaled

)

# --------------------------
# Accuracy
# --------------------------

accuracy = accuracy_score(

    y_encoded,

    prediction

)

print("\nTraining Accuracy :", round(accuracy*100,2),"%")

# --------------------------
# Classification Report
# --------------------------

print("\nClassification Report\n")

print(

    classification_report(

        y_encoded,

        prediction,

        target_names=label_encoder.classes_

    )

)

# --------------------------
# Confusion Matrix
# --------------------------

cm = confusion_matrix(

    y_encoded,

    prediction

)

disp = ConfusionMatrixDisplay(

    confusion_matrix=cm,

    display_labels=label_encoder.classes_

)

plt.figure(figsize=(10,8))

disp.plot(
    xticks_rotation=45
)

plt.tight_layout()

plt.show()

# --------------------------
# Feature Importance
# --------------------------

if best_model_name == "Random Forest":

    importance = best_model.feature_importances_

    feature_names = X.columns

    plt.figure(figsize=(10,6))

    plt.barh(

        feature_names,

        importance

    )

    plt.title("Feature Importance")

    plt.tight_layout()

    plt.show()

print("\nTraining Completed Successfully!")