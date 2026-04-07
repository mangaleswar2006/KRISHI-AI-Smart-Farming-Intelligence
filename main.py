print("STARTING PROGRAM...")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("Crop_recommendation.csv")
print(data.head())

# Split input and output
X = data.drop("label", axis=1)
y = data["label"]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)
print("Training Done")

# Check accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Test prediction (example values)
# Create input with proper column names
sample = pd.DataFrame(
    [[90, 40, 40, 25, 80, 6.5, 200]],
    columns=X.columns
)

# Predict
prediction = model.predict(sample)
print("Recommended Crop:", prediction[0], flush=True)

prices = {
    "rice": 20,
    "wheat": 18,
    "jute": 25
}

yield_per_acre = {
    "rice": 2000,
    "wheat": 1800,
    "jute": 1500
}

crop = prediction[0]

if crop in prices:
    profit = prices[crop] * yield_per_acre[crop]
    print("Estimated Profit: ₹", profit)