from flask import Flask, render_template

# Configuración de la aplicación Flask
app = Flask(__name__, template_folder='Templates')  # Creamos una instancia de Flask y especificamos la carpeta de plantillas

# Ruta para la página de inicio (HTML)
@app.route('/')  # Decorador para definir la ruta "/"
def home():
    return render_template('home.html')

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)  # Iniciamos la aplicación en modo debug, escuchando en todas las interfaces de red (0.0.0.0) en el puerto 8000
