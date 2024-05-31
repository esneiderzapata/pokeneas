from flask import Flask, jsonify, render_template
import random
import socket

app = Flask(__name__)

# Datos de ejemplo de Pokeneas
pokeneas = [
    {"id": 1, "nombre": "Bulbasaur", "altura": "0.7m", "habilidad": "Espesura", "imagen": "pokenea1.jpg", "frase": "Soy muy bello ome"},
    {"id": 2, "nombre": "Ivysaur", "altura": "1.0m", "habilidad": "Espesura", "imagen": "pokenea2.jpg", "frase": "Chiquito pero peligroso"},
    {"id": 3, "nombre": "Venusaur", "altura": "2.0m", "habilidad": "Espesura", "imagen": "pokenea3.jpg", "frase": "Estoy mamadisimo"},
    {"id": 4, "nombre": "Charmander", "altura": "0.6m", "habilidad": "Mar Llamas", "imagen": "pokenea4.jpg", "frase": "Viva el JUNIOR!!"},
    {"id": 5, "nombre": "Charmeleon", "altura": "1.1m", "habilidad": "Mar Llamas", "imagen": "pokenea5.jpg", "frase": "El nacional solo lleva troncos"},
    {"id": 6, "nombre": "Charizard", "altura": "1.7m", "habilidad": "Mar Llamas", "imagen": "pokenea6.jpg", "frase": "Joder tio , soy lo mejor"},
    {"id": 7, "nombre": "Squirtle", "altura": "0.5m", "habilidad": "Torrente", "imagen": "pokenea7.jpg", "frase": "Gokuuuu!! Maldicionnnnn"},
    {"id": 8, "nombre": "Wartortle", "altura": "1.0m", "habilidad": "Torrente", "imagen": "pokenea8.jpg", "frase": "Te quiere mucho Don Ramon"},
    {"id": 9, "nombre": "Blastoise", "altura": "1.6m", "habilidad": "Torrente", "imagen": "pokenea9.jpg", "frase": "Guapo , poderoso , majestuoso"},
    {"id": 10, "nombre": "Caterpie", "altura": "0.3m", "habilidad": "Polvo Escudo", "imagen": "pokenea10.jpg", "frase": "Hola mundo"}
]

# Obtener el id del contenedor
contenedor_id = socket.gethostname()

@app.route('/pokeneas', methods=['GET'])
def obtener_pokenea():
    pokenea = random.choice(pokeneas)
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    }
    return jsonify(response)

@app.route('/pokeneas/frase', methods=['GET'])
def mostrar_pokenea_frase():
    pokenea = random.choice(pokeneas)
    return render_template('pokenea.html', nombre=pokenea["nombre"], imagen=pokenea["imagen"], frase=pokenea["frase"], contenedor_id=contenedor_id)

if __name__ == "__main__":
    app.run(debug=True)
