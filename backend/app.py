from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite todas las solicitudes de origen cruzado; ajustar según sea necesario

@app.route('/api/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message')
    # Lógica sencilla para responder al mensaje del usuario
    if user_message:
        bot_reply = f"Entiendo que has dicho: {user_message}. ¡Interesante! ¿En qué más te puedo ayudar con tus productos orgánicos?"
        return jsonify({'reply': bot_reply})
    return jsonify({'reply': "No entendí tu mensaje. ¿Podrías intentar de nuevo?"}), 400

if __name__ == '__main__':
    app.run(debug=True)
