from flask import Flask
from flask import request, jsonify

import requests
import json
import re

app = Flask(__name__)

URL = 'https://api.telegram.org/bot683361381:AAEaVGfJ4WqmgwkLGki4ZQsSqNFDy5oc4tw/'


def send_message(chat_id, text='bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.methods == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
            send_message(chat_id, 'Hello my friend')
        
        return jsonify(r)
    return '<h1>You are welcome</h1>'


if __name__ == '__main__':
    app.run()
