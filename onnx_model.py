import onnxruntime as ort
import numpy as np
from PIL import Image

# Load model
session = ort.InferenceSession("model.onnx")
input_name = session.get_inputs()[0].name

# Load image
img = Image.open("leaf.jpg").convert("RGB")
img = img.resize((640, 640))

# Preprocess
img_array = np.array(img).astype(np.float32) / 255.0
img_array = np.transpose(img_array, (2, 0, 1))
img_array = np.expand_dims(img_array, axis=0)

# Predict
outputs = session.run(None, {input_name: img_array})
pred = outputs[0][0]

print("Raw Output:", pred)

# Get result
index = np.argmax(pred)
confidence = np.max(pred)

class_names = ["Background", "tomato desies", "health leaf", "potato desies"]

if class_names[index] == "health leaf":
    print("Leaf is healthy ✅")
elif class_names[index] == "tomato desies":
    print("Tomato leaf disease detected ⚠️")
elif class_names[index] == "potato desies":
    print("Potato leaf disease detected ⚠️")
else:
    print("Please capture leaf clearly")