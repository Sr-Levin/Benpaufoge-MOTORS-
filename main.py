from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bienvenido a BenPauFoge Motors 🚗</h1><p>Donde los motores vuelven a rugir.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
