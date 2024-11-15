from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola mundo"

@app.route("/usuario/registrar")
def usuario_registrar():
    return render_template("registroUsuario.html")

@app.route("/usuario/guardar", methods=["POST"])
def usuario_guardar():
    email = request.form["email"]
    password = request.form["password"]
    return f"usuario: {email}"

@app.route("/usuario/mostrar")
def usuario_mostrar():
    usuarios = ["Omar Sulca", "Norma Bartra"]
    return render_template("mostrarUsuario.html", usuarios=usuarios)
