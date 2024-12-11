from flask import Flask

# Crea una instancia de Flask
app = Flask(__name__)

# Define una ruta para la API
@app.route('/api/home', methods=['GET'])
def hola_mundo():
    return {"mensaje": "Hello World, my Name is Santiago Zurita!"}, 200

# Ejecuta el servidor si este archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)
