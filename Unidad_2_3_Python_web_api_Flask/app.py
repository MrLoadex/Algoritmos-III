from flask import render_template
import connexion

# Inicializa la aplicación de Connexion
app = connexion.App(__name__, specification_dir="./")
#app.add_api("swagger.yml")

# Obtén la aplicación de Flask contenida en la aplicación de Connexion
flask_app = app.app

@flask_app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    
    flask_app.run(host="0.0.0.0", port=8000, debug=True)