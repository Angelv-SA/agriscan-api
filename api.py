from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Stockage de la dernière mesure reçue
derniere_mesure = {}

@app.route('/')
def home():
    return "API active ✅"

@app.route('/api/mesures', methods=['POST'])
def recevoir_mesures():
    global derniere_mesure
    data = request.json
    print("✅ Données reçues :", data)
    derniere_mesure = data
    return jsonify({"status": "ok", "message": "Mesures enregistrées"}), 200

@app.route('/api/mesures', methods=['GET'])
def envoyer_mesure():
    if derniere_mesure:
        return jsonify(derniere_mesure), 200
    else:
        return jsonify({"status": "empty", "message": "Pas encore de mesure"}), 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
