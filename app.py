from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def buscar_producto(codigo):
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
    producto = cursor.fetchone()
    conn.close()
    return producto

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", producto=None, mensaje=None)

@app.route("/buscar", methods=["POST"])
def buscar():
    codigo = request.form["codigo"]
    producto = buscar_producto(codigo)
    if producto:
        return render_template("index.html", producto=producto)
    else:
        return render_template("index.html", producto=None, mensaje="Producto no encontrado")

if __name__ == "__main__":
    app.run(debug=True)
