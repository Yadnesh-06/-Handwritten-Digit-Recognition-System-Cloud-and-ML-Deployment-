from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
import logging

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GPU Configuration (Optional)
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# Uncomment below to specify GPU device or run on CPU only
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Use GPU 0
# os.environ["CUDA_VISIBLE_DEVICES"] = ""   # Use CPU only

app = Flask(__name__, static_folder="static", template_folder="templates")

# Enable CORS
CORS(app)

# Load the pre-trained model
try:
    model = load_model('model.h5.keras', compile=False)
    logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise RuntimeError(f"Failed to load model. Error: {str(e)}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if an image is uploaded
        if 'image' not in request.files:
            logger.warning("No image uploaded.")
            return jsonify({'error': 'No image uploaded'}), 400

        file = request.files['image']

        try:
            image = Image.open(file).convert('L')  # Convert to grayscale
        except Exception as e:
            logger.warning(f"Invalid image format: {e}")
            return jsonify({'error': 'Invalid image format'}), 400

        # Preprocess the image
        image = image.resize((28, 28))  # Resize to 28x28
        image = np.array(image, dtype=np.float32) / 255.0  # Normalize

        # Flatten the image if the model expects (None, 784)
        if model.input_shape == (None, 784):  # Flattened input
            image = image.reshape(1, 784)
        elif model.input_shape == (None, 28, 28, 1):  # 28x28x1 input
            image = image.reshape(1, 28, 28, 1)
        else:
            logger.error(f"Unexpected model input shape: {model.input_shape}")
            return jsonify({'error': f'Unexpected model input shape: {model.input_shape}'}), 500

        # Make a prediction
        prediction = model.predict(image)
        digit = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        logger.info(f"Prediction successful. Digit: {digit}, Confidence: {confidence:.2f}")

        return jsonify({'digit': digit, 'confidence': confidence})

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
