from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

gradio_client = Client("https://wizzseen-stock.hf.space/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json.get('input_data', '')
    
    result = gradio_client.predict(input_data, api_name="/predict")
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
