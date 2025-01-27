from flask import Flask

app = Flask(__name__)

@app.route("/")

def pagina_inicial():
    return "Arrumando o Continuous Integration and Continuous Delivery"