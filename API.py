from flask import Flask, jsonify, request

app = Flask(__name__)

from alumnos import alumnos

@app.route("/")
def root ():
     return "bienbenidos"

@app.route("/alumnos")
def getAlumnos():
    return jsonify(alumnos)

## BUSCAR UN ALUMNO
@app.route("/alumnos/<string:alumno_name>")
def getalumno(alumno_name):
    alumnofound = [alumno for alumno in alumnos if alumno ["Nombre"] == alumno_name]
    if (len(alumnofound) > 0):
        return jsonify ({"alumno": alumnofound[0]})

## AGREGAR UN ALUMNO 
@app.route("/alumnos", methods=["POST"])
def addalumno():
    new_alumno ={
        "Nombre": request.json["Nombre"],
        "Especialidad": request.json["Especialidad"],
        "Matricula": request.json["Matricula"],
        "Grupo": request.json["Grupo"]
    }
    alumnos.append(new_alumno)
    return jsonify({"mensaje": "alumno agregado satisfactoriamente", "alumnos":alumnos})

## Actualizar UN ALUMNO
@app.route("/alumnos/<string:alumno_name>", methods=["PATCH"])
def patchalumno(alumno_name):
    alumno_found = [alumno for alumno in alumnos if alumno["Nombre"] == alumno_name]
    if len(alumno_found) > 0:
        alumno_actualizado = {}
        for key, value in request.json.items():
            alumno_actualizado[key] = value
        alumno_found[0].update(alumno_actualizado)
        return jsonify({
            "mensaje": "Alumno Actualizado satisfactoriamente",
            "alumno": alumno_found[0]
        })

    
## ELIMINAR UN ALUMNO
@app.route("/alumnos/<string:alumno_name>", methods=["DELETE"])
def eliminalumno(alumno_name):
    alumnosfound = [alumno for alumno in alumnos if alumno["Nombre"] == alumno_name]
    if len(alumnosfound) > 0:
        alumnos.remove(alumnosfound[0])
        return jsonify({
            "mensaje": "Alumno Eliminado",
            "alumnos": alumnos  
                    })
    

if __name__ == "__main__":
    app.run(debug=True)