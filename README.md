# Image-Classification
📌 Project Overview

This project is an Image Classification Web App built using Django and a pre-trained Machine Learning model. The model is trained on the CIFAR-10 dataset, which consists of 10 different object categories. The web application allows users to upload an image, and the system predicts its category.
🚀 Features

✅ Upload an image for classification
✅ Uses a trained model to predict the image category
✅ Provides real-time results with user-friendly UI
✅ Supports 10 classes from the CIFAR-10 dataset
✅ Built with Django for seamless backend processing
🔍 Supported Image Categories

This model is trained on the CIFAR-10 dataset, which consists of the following categories:

    ✈️ Airplane
    🚗 Automobile
    🐦 Bird
    🐱 Cat
    🦌 Deer
    🐶 Dog
    🐸 Frog
    🐴 Horse
    🚢 Ship
    🚚 Truck

🛠️ Tech Stack

    Frontend: HTML, CSS
    Backend: Django
    Model: Pre-trained ML model using CIFAR-10
    Dependencies: Pillow, NumPy, Joblib



📂 Project Structure

├── classifier/             # Django app for classification
│   ├── templates/          # HTML files
│   │   ├── upload.html     # Upload form UI
│   ├── views.py            # Backend logic for image classification
│   ├── urls.py             # URL routing
├── static/                 # Static assets (CSS, JS, images)
├── classifier/model.pkl    # Trained CIFAR-10 model
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
