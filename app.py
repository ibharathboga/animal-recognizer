from flask import Flask, render_template, request, redirect, url_for
from arecognizer import identifyAnimal

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('main.html')

@app.route('/upload', methods=["POST"])
def upload():
    image = request.files['ImageFile']
    image_path = "static/images/" + "UploadedImage.jpg"
    print(f"Uploaded Image Name: {image.filename}")
    image.save(image_path)
    return redirect(url_for('results', image_path=image_path))

@app.route('/results', methods=["GET"])
def results():
    image_path = request.args.get('image_path')
    modelOutput = identifyAnimal(image_path)
    print(f"Model Prediction Output:\n{modelOutput}")
    return render_template("show.html", uploaded=True, iname="UploadedImage.jpg", animal=modelOutput)

if __name__ == '__main__':
    app.run(debug=True)


