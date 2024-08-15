from Flask import Flask, request, jsonify # type: ignore

apps = Flask(__name__)

# Base de datos simulada de usuarios en memoria (clave-valor)
users_db = {}

@apps.route('/api/register', methods=['POST'])
def register():
    """
    Ruta para registrar un nuevo usuario.
    Recibe un JSON con 'username' y 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Verificar si el usuario ya existe
    if username in users_db:
        return jsonify({"error": "Usuario ya registrado"}), 400
    
    # Registrar el nuevo usuario
    users_db[username] = password
    return jsonify({"message": "Registro exitoso"}), 201

@apps.route('/api/login', methods=['POST'])
def login():
    """
    Ruta para iniciar sesión.
    Recibe un JSON con 'username' y 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Verificar si el usuario existe y la contraseña es correcta
    if users_db.get(username) == password:
        return jsonify({"message": "Autenticación satisfactoria"}), 200
    else:
        return jsonify({"error": "Error en la autenticación"}), 401

if __name__ == '__main__':
    apps.run(debug=True)