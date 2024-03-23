import os
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}

def generate_response(prompt):
    data = {
        "model": "CodeAssist",
        "prompt": prompt,
        "stream" : False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        return actual_response
    else:
        return "Error: " + response.text

@app.route('/', methods=['POST'])
def predict():
    prompt = request.form.get('prompt')
    if prompt:
        response = generate_response(prompt)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Prompt is required'}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
