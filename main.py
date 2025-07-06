
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1391203448632115323/iIpYNhK7t0G9JmryTXmB2eXK6rEgkQC71RO6llw7hqRClhzqtAVbH_xW6XHFIdA1rZ4s'

def enviar_a_discord(empleado, fecha, vehiculo, trabajo):
    embed = {
        "title": "🛠️ REPORTE DE TRABAJO DEL ESTADO 💸 PAGO INMEDIATO 💸",
        "color": 15158332,
        "fields": [
            {"name": "👨‍🔧 Empleado", "value": empleado, "inline": True},
            {"name": "📅 Fecha", "value": fecha, "inline": True},
            {"name": "🚗 Vehículo", "value": vehiculo, "inline": True},
            {"name": "📦 Trabajo realizado", "value": trabajo, "inline": False}
            "title": "📸 Foto adjunta: (subir captura del trabajo realizado en RP)",
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
