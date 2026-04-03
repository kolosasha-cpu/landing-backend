from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с нашего сайта на GitHub Pages

# Берём токен и chat_id из переменных окружения (как у бота)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')


@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные из формы
    data = request.get_json()

    name    = data.get('name', 'не указано')
    phone   = data.get('phone', 'не указано')
    email   = data.get('email', 'не указано')
    message = data.get('message', 'не указано')

    # Формируем красивое сообщение для Telegram
    text = (
        f"📬 Новая заявка с сайта!\n\n"
        f"👤 Имя: {name}\n"
        f"📞 Телефон: {phone}\n"
        f"✉️ Email: {email}\n"
        f"💬 Сообщение: {message}"
    )

    # Отправляем сообщение в Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        'chat_id': CHAT_ID,
        'text': text
    })

    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True)