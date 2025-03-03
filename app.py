from flask import Flask, request

app = Flask(__name__)

# Page principale
@app.route('/')
def home():
    visitor_ip = request.remote_addr  # Récupère l'IP du visiteur
    with open("logs.txt", "a") as log:
        log.write(f"Nouvelle visite : {visitor_ip}\n")  # Enregistre l'IP
    return f"<h1>Bienvenue !</h1><p>Ton IP a été enregistrée 😏</p>"

# Lance le serveur
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
