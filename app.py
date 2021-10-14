import pickle
import numpy as np
from flask import Flask, request, jsonify

model = None
app = Flask(__name__)


def load_model():
    global model
    # model variable refers to the global variable
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json(force=True)
        s1 = data['s']
        result = model.predict_sentiment(s1)[0]
        final = {"Label":result}
        print(final)
    return jsonify(final)


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=5000)
