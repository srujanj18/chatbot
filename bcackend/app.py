from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
# app.py
OPENAI_API_KEY = "your_api_key_here"  # REMOVE THIS LINE


@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.json.get('question')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Answer this question: {user_question}",
        max_tokens=150
    )
    return jsonify({'answer': response.choices[0].text.strip()})

@app.route('/quiz', methods=['GET'])
def get_quiz():
    with open('data/subjects.json', 'r') as f:
        content = f.read()
    return jsonify({'quiz': content})

if __name__ == '__main__':
    app.run(debug=True)
