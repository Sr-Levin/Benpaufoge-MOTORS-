
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/tu_webhook_aqui'

def enviar_a_discord(empleado, fecha, vehiculo, trabajo):
    embed = {
        "title": "🛠️ REPORTE DE TRABAJO: REPARACIÓN EN CARRETERA",
        "color": 15158332,
        "fields": [
            {"name": "👨‍🔧 Empleado", "value": empleado, "inline": True},
            {"name": "📅 Fecha", "value": fecha, "inline": True},
            {"name": "🚗 Vehículo", "value": vehiculo, "inline": True},
            {"name": "📦 Trabajo realizado", "value": trabajo, "inline": False}
        ]
    }
    data = {"embeds": [embed]}
    requests.post(WEBHOOK_URL, json=data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reporte', methods=['POST'])
def reporte():
    empleado = request.form['empleado']
    fecha = request.form['fecha']
    vehiculo = request.form['vehiculo']
    trabajo = request.form['trabajo']

    enviar_a_discord(empleado, fecha, vehiculo, trabajo)
    return redirect('/')

if __name__ == '__main__':
    app.run()
