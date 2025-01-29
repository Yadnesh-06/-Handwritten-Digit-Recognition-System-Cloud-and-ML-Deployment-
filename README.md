# Handwritten Digit Recognition

## 📌 Project Overview
This project is a **Handwritten Digit Recognition** system using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. The model is deployed using **Flask**, containerized with **Docker**, and orchestrated with **Kubernetes (Minikube)**.

## 🚀 Features
- **Digit Recognition**: Identifies digits (0-9) from images.
- **REST API**: Built with Flask to handle image uploads and return predictions.
- **Containerized Deployment**: Uses Docker for portability.
- **Kubernetes Orchestration**: Uses Minikube to manage services.

---

## 🛠️ Technologies Used
- **Python**
- **TensorFlow / Keras**
- **Flask**
- **Docker**
- **Kubernetes (Minikube)**
- **Kompose**
- **Postman (for API testing)**

---

## 🖥️ **1. Setup Instructions**

### **🔹 Clone the Repository**
git clone https://github.com/YOUR_GITHUB_USERNAME/Handwritten-Digit-Recognition.git
cd Handwritten-Digit-Recognition

🔹 Install Dependencies
Make sure you have Python installed, then install the required packages:
pip install -r requirements.txt

🔹 Run Flask App (Without Docker)
python app.py
The app will be available at http://127.0.0.1:5000.

## 🐳 **2. Running with Docker**
🔹 Build and Run Docker Container
docker build -t digit-recognition-app .
docker run -p 5000:5000 digit-recognition-app
The API will be accessible at http://127.0.0.1:5000.

## 🐙 **3. Running with Docker Compose**
If you have docker-compose.yml, you can spin up the entire setup:
docker-compose up --build
This automatically builds and runs the container.

## ☸️ **4. Deploying with Kubernetes (Minikube)**
🔹 Step 1: Start Minikube
minikube start

🔹 Step 2: Build Docker Image in Minikube
eval $(minikube docker-env)
docker build -t digit-recognition-app .

🔹 Step 3: Convert docker-compose.yml to Kubernetes Manifests
If you used Kompose, run:
kompose convert
This generates deployment.yaml and service.yaml.

🔹 Step 4: Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

🔹 Step 5: Expose the Service
kubectl get services
minikube service app
