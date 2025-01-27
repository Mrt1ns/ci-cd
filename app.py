<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
@app.route("/")
def pagina_inicial():
    return "Desafio Custom Message"
=======
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Desafio Custom Message"
>>>>>>> 4c60bf608fada749e00205d1ca50afcb5c81873f