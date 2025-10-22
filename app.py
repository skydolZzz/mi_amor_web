from flask import Flask, render_template, jsonify
import json
import os  # Necesario para leer el puerto de Render

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/garden')
def garden():
    with open('data/garden.json', encoding='utf-8') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render asigna el puerto
    app.run(host='0.0.0.0', port=port, debug=True)
