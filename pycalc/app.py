"""API web mínima de pycalc.

Ejemplos:
    GET /              -> información de la app
    GET /add/2/3       -> {"resultado": 5.0}
    GET /divide/1/0    -> 400, {"error": "No se puede dividir entre cero"}
"""

from flask import Flask, jsonify

from pycalc import calc

app = Flask(__name__)

OPERACIONES = {
    "add": calc.add,
    "subtract": calc.subtract,
    "multiply": calc.multiply,
    "divide": calc.divide,
    "power": calc.power,
}


@app.get("/")
def index():
    return jsonify(app="pycalc", version="1.3", operaciones=list(OPERACIONES))


@app.get("/<op>/<a>/<b>")
def operar(op: str, a: str, b: str):
    if op not in OPERACIONES:
        return jsonify(error=f"Operación desconocida: {op}"), 404
    try:
        resultado = OPERACIONES[op](float(a), float(b))
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
