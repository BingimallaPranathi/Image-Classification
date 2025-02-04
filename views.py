from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
from PIL import Image
import numpy as np
import io

# Load the model (adjust the path if necessary)
model = joblib.load('classifier/model.pkl')

# Define class labels corresponding to the model's output
class_labels = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

@csrf_exempt
def classify_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return render(request, 'classifier/upload.html', {'error': 'No image provided'})
        
        image_file = request.FILES['image']

        try:
            image = Image.open(image_file)
        except Exception as e:
            return render(request, 'classifier/upload.html', {'error': f'Invalid image format: {str(e)}'})

        try:
            # Resize the image to the expected input size
            image = image.resize((32, 32))  # Change the size to 32x32
            image_array = np.array(image)
            image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

            # Predict using the model
            prediction = model.predict(image_array)
            predicted_index = np.argmax(prediction)  # Get the index of the highest value
            predicted_label = class_labels[predicted_index]  # Get the corresponding class label

            return render(request, 'classifier/upload.html', {'prediction': predicted_label})
        except Exception as e:
            return render(request, 'classifier/upload.html', {'error': f'Error during prediction: {str(e)}'})

    # For GET request, render the form
    return render(request, 'classifier/upload.html')
