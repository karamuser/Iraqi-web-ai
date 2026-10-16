from flask import Flask, render_template, request, jsonify
from core.ai_engine import AIEngine
import os

app = Flask(__name__, template_folder='../ui', static_folder='../ui', static_url_path='')
ai_engine = AIEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_text = data.get('message', '')
    grade_level = data.get('grade', 'السادس_الإعدادي')

    if not user_text:
        return jsonify({'error': 'الرسالة فارغة'}), 400

    response_text = ai_engine.generate_response(user_text, grade_level)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
    
