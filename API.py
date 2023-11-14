from flask import Flask, jsonify, request

app = Flask(__name__)

from alumnos import alumnos

@app.route("/")
def root ():
     return "bienbenidos"

@app.route("/alumnos")
def getAlumnos():
    return jsonify(alumnos)


if __name__ == "__main__":
    app.run(debug=True)