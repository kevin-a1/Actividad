from flask import Flask, render_template, request
import json

datos = {
    "1" : "Python",
    "2" : "Java",
    "3" : "PHP",
    "4" : "JavaScript",
    "5" : "C++"}

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

def key(datos):
    data = datos.keys()
    con = len(data)
    con = con + 1
    return con

@app.route('/agregar', methods=["GET"])
def agregar():
    try:
        lenguaje = str(request.args.get('lenguaje'))
        print(datos)
        datos[key(datos)] = lenguaje
        sin_codi = json.dumps(datos)
        return json.loads(sin_codi)
    except:
        sin_codi = json.dumps(datos)
        return json.loads(sin_codi)

@app.route('/listar')
def listar():
    sin_codi = json.dumps(datos)
    return json.loads(sin_codi)
