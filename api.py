from fastapi import FastAPI, File, UploadFile
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import onnxruntime as ort
import numpy as np
from PIL import Image
import io

app = FastAPI()

# =========================
# 🌱 LOAD CROP MODEL
# =========================
data = pd.read_csv(r"C:\krishi\Crop_recommendation.csv")

X = data.drop("label", axis=1)
y = data["label"]

crop_model = RandomForestClassifier()
crop_model.fit(X, y)

# =========================
# 🍃 LOAD DISEASE MODEL (ONNX)
# =========================
session = ort.InferenceSession(r"C:\krishi\model.onnx")
input_name = session.get_inputs()[0].name

# ⚠️ VERY IMPORTANT (from your label_map)
class_names = [
    "Background",
    "tomato desies",
    "health leaf",
    "potato desies"
]

# =========================
# 🏠 HOME ROUTE
# =========================
@app.get("/")
def home():
    return {"message": "Krishi AI Combined API Running 🚀"}

# =========================
# 🌱 CROP PREDICTION
# =========================
@app.post("/crop")
def predict_crop(
    N: int,
    P: int,
    K: int,
    temperature: float,
    humidity: float,
    ph: float,
    rainfall: float
):

    sample = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=X.columns
    )

    prediction = crop_model.predict(sample)[0]

    return {
        "recommended_crop": prediction,
        "message": f"Best crop to grow is {prediction} 🌾"
    }

# =========================
# 🍃 DISEASE DETECTION
# =========================
@app.post("/disease")
async def detect_disease(file: UploadFile = File(...)):

    contents = await file.read()

    # Load image
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((640, 640))   # ⚠️ must match model

    # Preprocess
    img_array = np.array(img).astype(np.float32) / 255.0
    img_array = np.transpose(img_array, (2, 0, 1))
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    outputs = session.run(None, {input_name: img_array})
    pred = outputs[0][0]

    index = int(np.argmax(pred))
    confidence = float(np.max(pred))

    label = class_names[index]

    # Smart response
    if label == "health leaf":
        result = "Leaf is healthy ✅"
    elif label == "tomato desies":
        result = "Tomato leaf disease detected ⚠️"
    elif label == "potato desies":
        result = "Potato leaf disease detected ⚠️"
    else:
        result = "Please capture leaf clearly"

    return {
        "prediction": label,
        "message": result,
        "confidence": confidence
    }