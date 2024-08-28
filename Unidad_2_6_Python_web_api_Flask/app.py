import config
from flask import render_template, request, url_for, redirect
# from models import Person
from people import read_all, create, delete
from notes import read_one, read_one_by_user_lname

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', people=read_all())

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        new_person = {
            "fname": fname,
            "lname": lname
        }
        create(new_person)
        return redirect(url_for('agregar'))
    
    return render_template('agregar.html', people=read_all())

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        lname = request.form['lname']
        delete(lname)
        return redirect(url_for('eliminar'))
    return render_template('eliminar.html', people=read_all())

@app.route('/seleccionar_notas', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':
        lname = request.form['lname']
        return redirect(url_for('get_note_by_person_lname', lname=lname))
    return render_template('seleccionar_notas.html', people=read_all())

@app.route('/notes/person/<lname>', methods=['GET'])
def get_note_by_person_lname(lname):
    notes = read_one_by_user_lname(lname)
    return render_template('nota.html', notas=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
