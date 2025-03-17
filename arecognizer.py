from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input

import numpy as np
import pandas as pd

ANIMAL_TAGS_PATH = r"model\AnimalTags.csv"
#MODEL_PATH = r"model\AnimalRecognizer.h5"
MODEL_PATH = r"model\AnimalRecognizerModel.h5"

model = load_model(MODEL_PATH)
df = pd.read_csv(ANIMAL_TAGS_PATH)

def identifyAnimal(image):
    #preprocess image
    img = load_img(image, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    image = preprocess_input(img)
    #output
    modelOutput = model.predict(image,verbose = 0)
    labelID = np.argmax(modelOutput)
    animal = df.loc[labelID]
    return animal.to_dict()

