<div align="center">

<img src="https://img.shields.io/badge/KRISHI_AI-🌾_Smart_Farming_Intelligence-2d6a4f?style=for-the-badge&labelColor=1b4332" alt="KRISHI AI Banner"/>

# 🌾 KRISHI AI — Smart Farming Intelligence

**AI-powered crop recommendation & plant disease detection for modern agriculture**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-005571?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![ONNX](https://img.shields.io/badge/ONNX-Runtime-005CED?style=flat-square&logo=onnx)](https://onnxruntime.ai/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-RandomForest-F7931E?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> 🌱 Helping farmers make smarter decisions — from soil to harvest.

---

</div>

## 📖 About

**KRISHI AI** (कृषि = *Agriculture* in Sanskrit/Hindi) is an intelligent farming assistant that uses machine learning to:

- 🌾 **Recommend the best crop** based on soil & weather parameters (N, P, K, temperature, humidity, pH, rainfall)
- 🍃 **Detect plant diseases** from leaf images using a deep learning ONNX model
- 🤖 **Expose REST APIs** via FastAPI for easy integration with mobile apps, robots, or dashboards

Originally built to integrate with **Choregraphe / NAO Robots** for automated farm diagnosis, KRISHI AI is flexible enough to work with any frontend or IoT device.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🌱 Crop Recommendation | Random Forest model trained on real agricultural data |
| 🍃 Disease Detection | ONNX deep learning model — detects Tomato & Potato leaf diseases |
| ⚡ REST API | FastAPI-powered, auto-documented Swagger UI at `/docs` |
| 🤖 Robot-Ready | Designed for Choregraphe Python box integration |
| 🔬 Offline Inference | Runs fully locally — no cloud required |

---

## 🏗️ Project Structure

```
krishi-ai/
│
├── api.py                  # 🚀 FastAPI server (crop + disease endpoints)
├── main.py                 # 🧪 Standalone training & crop prediction script
├── onnx_model.py           # 🍃 Raw ONNX inference test script
│
├── Crop_recommendation.csv # 📊 Training dataset (soil & climate parameters)
├── model.onnx              # 🧠 Disease detection deep learning model (ONNX)
├── label_map.pbtxt         # 🏷️ Class label map for disease model
├── leaf.jpg                # 🖼️ Sample leaf image for testing
│
├── requirements.txt        # 📦 Python dependencies
└── .gitignore              # 🚫 Files excluded from git
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/krishi-ai.git
cd krishi-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the ONNX Model

> ⚠️ The `model.onnx` file is large and excluded from git. Download it separately and place it in the project root.

```
krishi-ai/
└── model.onnx   ← Place here
```

---

## 🌐 Running the API Server

```bash
uvicorn api:app --reload
```

Then open your browser at:

- 📄 **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 🔍 **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints

### 🏠 `GET /`
Health check — confirms the API is running.

```json
{ "message": "Krishi AI Combined API Running 🚀" }
```

---

### 🌾 `POST /crop` — Crop Recommendation

Predicts the most suitable crop based on soil and environmental parameters.

**Query Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `N` | int | Nitrogen content in soil |
| `P` | int | Phosphorus content in soil |
| `K` | int | Potassium content in soil |
| `temperature` | float | Temperature in °C |
| `humidity` | float | Relative humidity (%) |
| `ph` | float | Soil pH value |
| `rainfall` | float | Annual rainfall (mm) |

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/crop?N=90&P=40&K=40&temperature=25&humidity=80&ph=6.5&rainfall=200"
```

**Example Response:**
```json
{
  "recommended_crop": "rice",
  "message": "Best crop to grow is rice 🌾"
}
```

---

### 🍃 `POST /disease` — Plant Disease Detection

Upload a leaf image to detect whether it is healthy or diseased.

**Form Data:**

| Field | Type | Description |
|---|---|---|
| `file` | image | JPG/PNG leaf image |

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/disease" \
  -F "file=@leaf.jpg"
```

**Example Response:**
```json
{
  "prediction": "tomato desies",
  "message": "Tomato leaf disease detected ⚠️",
  "confidence": 0.94
}
```

**Supported Classes:**

| Class | Description |
|---|---|
| `health leaf` | Plant is healthy ✅ |
| `tomato desies` | Tomato leaf disease detected ⚠️ |
| `potato desies` | Potato leaf disease detected ⚠️ |

---

## 🧪 Running Standalone Scripts

### Crop Recommendation (offline)
```bash
python main.py
```

### Disease Detection (offline, uses `leaf.jpg`)
```bash
python onnx_model.py
```

---

## 🤖 Choregraphe / NAO Robot Integration

KRISHI AI was built to work with **SoftBank Robotics NAO** via Choregraphe Python boxes.

The robot can:
1. Capture a leaf image
2. Send it to the `/disease` API endpoint
3. Announce the diagnosis via **Text-to-Speech**

> See the Choregraphe Python box script in the [integration guide](#) (coming soon).

---

## 🗺️ Workflow

```mermaid
graph TD
    A[🌾 Farmer Input] -->|Soil & Climate Data| B[/crop API]
    A -->|Leaf Photo| C[/disease API]
    B --> D[Random Forest Model]
    C --> E[ONNX Disease Model]
    D --> F[🌱 Crop Recommendation]
    E --> G[🍃 Disease Result + Confidence]
    F --> H[📱 App / Robot / Dashboard]
    G --> H
```

---

## 📊 Dataset

The crop recommendation model is trained on the **Crop Recommendation Dataset** which includes:

- **Features:** N, P, K, temperature, humidity, pH, rainfall
- **Target:** Crop label (22 crop types including rice, wheat, maize, etc.)
- **Size:** ~2,200 rows

---

## 🛣️ Roadmap

- [x] Crop recommendation REST API
- [x] Plant disease detection via ONNX
- [x] Choregraphe robot integration
- [ ] Frontend web dashboard
- [ ] Multi-language support (Hindi, Marathi)
- [ ] Weather API integration for real-time data
- [ ] Mobile app (Flutter)
- [ ] More disease classes (wheat, corn, etc.)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork this repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request 🚀

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ for Indian farmers 🇮🇳

**KRISHI AI** — *Empowering Agriculture with Artificial Intelligence*

</div>
