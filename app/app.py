from flask import Flask, render_template, jsonify, request

import config
import database

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/desafio")
def desafio():
    return render_template("desafio.html")


@app.route("/health")
def health():
    return render_template("health.html")


@app.route("/api/info")
def api_info():
    return jsonify(
        {
            "application": "Donde esta el Secret",
            "version": "1.0.0",
            "status": "running",
            "conference": "DojoConf"
        }
    )
@app.route("/employees")
def employees():

    employees = database.get_employees()

    return render_template(
        "employees.html",
        employees=employees
    )


@app.route("/admin")
def admin():

    key = request.args.get("key")

    if key != config.ADMIN_API_KEY:
        return render_template("unauthorized.html"), 401

    stats = {
        "database": "Connected",
        "employees": database.count_employees(),
        "version": "1.0.0",
        "environment": "Production"
    }

    challenge = {

        "message":
        "¡Reto completado! Encontraste un secreto válido expuesto en el código fuente.",


        "authentication":
        "ADMIN_API_KEY aceptada correctamente",


        "secret_location":
        "Archivo de configuración dentro del repositorio",


        "database_access":
        "Acceso autorizado a la base de datos",


        "risk":
        "Credenciales almacenadas directamente en la aplicación"

    }

    return render_template(
        "admin.html",
        stats=stats,
        challenge=challenge
    )


@app.route("/api/internal")
def internal():

    key = request.args.get("key")

    if key != config.INTERNAL_API_KEY:
        return jsonify({"error":"Unauthorized"}),401

    return jsonify({"message":"Internal API"})

@app.route("/payroll")
def payroll():

    token = request.args.get("token")

    if token != config.SERVICE_TOKEN:
        return jsonify({"error":"Unauthorized"}),401

    return jsonify({"message":"Payroll Service"})

@app.route("/storage")
def storage():

    key = request.args.get("key")

    if key != config.STORAGE_ACCESS_KEY:
        return jsonify({"error":"Unauthorized"}),401

    return jsonify({"message":"Storage"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
