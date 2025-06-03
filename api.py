from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API active ✅"

@app.route('/api/mesures', methods=['POST'])
def recevoir_mesures():
    data = request.json
    print("✅ Données reçues :", data)
    return jsonify({"status": "ok", "message": "Mesures enregistrées"}), 200

# 👇 Partie importante pour Render
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
