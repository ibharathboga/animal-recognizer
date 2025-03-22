# Model Description

This model is a fine-tuned version of the VGG16 architecture on the Animal Image Dataset (90 Different Animals)
from Kaggle. VGG16 is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from the University of Oxford.

# Limitations

- Generalization: The model is trained specifically on the Animal Image Dataset (90 Different Animals) dataset and may not generalize well to animals not included in this dataset or images with significantly different characteristics (e.g., different lighting, angles, or backgrounds).

- Biases: Performance may vary across different fruit categories due to the distribution and quality of the dataset images.

# Training and Evaluation Data

The model was trained and evaluated on the Animal Image Dataset (90 Different Animals). This dataset contains over 5400 Animal Images in 90 different categories or classes, split into training and test sets.

## Dataset Statistics

- Training Set: 3,456 images
- Validation Set: 864 images
- Test Set: 1,080 images

# Data Augmentation

- Preprocessing: All images were preprocessed using the preprocess_input function from the VGG16 module.
- Augmentation: Images were augmented with random rotations, shifts, zooms, flips, and more to improve the model's generalization.

# To use the model via flask based application

- Open command prompt in administrator mode.

## run the following commands

- create a virtual environment
  `python -m venv venvOne`

- activate the virtual environment
  `.\env\Scripts\activate`

- install libraries using requirements.txt
  `pip install -r requirements.txt`

- run the app
  `python app.py`
