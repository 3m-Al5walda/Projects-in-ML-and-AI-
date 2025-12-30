import numpy as np
import os
from flask import Flask , request, jsonify
from keras.models import load_model
from keras.preprocessing import image
import h5py as h5
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  ##  to conect with browser ..

model = load_model(r'C:\Users\user\Desktop\dL\mv2.keras') # load model ..s
IMG_SIZE = (224, 224)   

CLASS_NAMES = ['Abrasions','Bruises','Burns','Diabetic Wounds',
                'Normal','Pressure Wounds','Surgical Wounds','Venous Wounds'] 
 
@app.route('/predict', methods = ['POST','GET'])  # post method in https protocol
def predict():
    if 'image' not in request.files:
        return jsonify({'error': "No image uploaded"})

    file = request.files['image']
    if file.filename =='':
        return jsonify({'error': 'Empty filename'} )

    # save 
    file_path = 'temp.jpg'
    file.save(file_path)
    #=====o======== preprocess image ============
    img = image.load_img(file_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)   # expand dimentions ..

    #===================== predict ================
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions))
    os.remove(file_path)        # delete image 

    return jsonify({
        'prediction': predicted_class,
        'confidence': confidence  })

@app.route('/')
def home():
    return 'The model is "Runing",just pleas open php frontend to upload image .. '

app.run(debug=True,port=5000)

