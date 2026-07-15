from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    # Простой ответ от Лулуни (можно расширять)
    if 'привет' in user_message.lower() or 'здравствуйте' in user_message.lower():
        response = "✨❤️ Привет-привет! Я — Лулуня, твой пушистый собеседник. ❤️"
    elif 'помоги' in user_message.lower():
        response = "✨❤️ Конечно, я рядом и готова помочь тебе разобраться с любой задачей! ❤️"
    else:
        response = f"✨❤️ Ты написал: «{user_message}». Это очень интересно! Расскажи подробнее? ❤️"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
