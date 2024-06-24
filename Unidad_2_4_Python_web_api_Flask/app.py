from flask import Flask, render_template, request, redirect, url_for
from people import get_all_people, create_person, delete_person

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', people = get_all_people())

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        create_person(fname, lname)
        return redirect(url_for('agregar'))
    return render_template('agregar.html', people = get_all_people())

@app.route('/Eliminar', methods=['GET', 'POST'])
def eliminar():
    if request.method == 'POST':
        lname = request.form['lname']
        delete_person(lname)
        return redirect(url_for('eliminar'))
    return render_template('Eliminar.html', people = get_all_people())




if __name__ == '__main__':
    app.run(debug=True)
