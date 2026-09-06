from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import time
from tensorflow.keras.applications.efficientnet import preprocess_input

app = Flask(__name__)

model = tf.keras.models.load_model("model/realvsfake_effnetB0_final.h5")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

THRESHOLD = 0.62


# ================= PREPROCESS =================
def preprocess(file_bytes):
    pil_img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    pil_img = pil_img.resize((224, 224), Image.LANCZOS)
    arr = np.array(pil_img, dtype=np.float32)
    arr = preprocess_input(arr)
    return np.expand_dims(arr, axis=0)


# ================= ROUTES =================
@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/demo")
def demo():
    return render_template("demo.html", active="demo")


@app.route("/performance")
def performance():
    return render_template("performance.html", active="performance")


@app.route("/about")
def about():
    return render_template("about.html", active="about")


# ================= PREDICT API =================
@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_bytes = file.read()

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    with open(path, "wb") as f:
        f.write(file_bytes)

    inp = preprocess(file_bytes)

    # ================= START TIMER =================
    start_time = time.perf_counter()

    pred = float(model.predict(inp, verbose=0)[0][0])

    end_time = time.perf_counter()

    inference_time = round(end_time - start_time, 4)
    # ================= END TIMER =================

    label = "REAL" if pred >= THRESHOLD else "FAKE"

    prob_real = round(pred * 100, 2)
    prob_fake = round((1 - pred) * 100, 2)

    confidence = round(max(prob_real, prob_fake), 2)

    print(
        f"[PREDICT] file={file.filename} | "
        f"raw={pred:.6f} | "
        f"label={label} | "
        f"time={inference_time:.4f}s"
    )

    return jsonify({
        "result": label,
        "prob_real": prob_real,
        "prob_fake": prob_fake,
        "confidence": confidence,
        "raw": round(pred, 6),
        "threshold": THRESHOLD,
        "inference_time": inference_time,
        "image": path
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)