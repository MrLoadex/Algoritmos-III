import sqlite3
from datetime import datetime

DATABASE = 'database.db'

# Función para conectar a la base de datos
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
    return conn

# Función para obtener todas las personas
def get_all_people():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM people')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Función para agregar una persona a la base de datos
def create_person(fname, lname):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO people (fname, lname, timestamp) VALUES (?, ?, ?)', (fname, lname, timestamp))
    conn.commit()
    conn.close()

# Función para obtener una persona por su ID
def get_person_by_id(person_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM people WHERE id = ?', (person_id,))
    row = cursor.fetchone()
    conn.close()
    return row if row else None

# Función para obtener una persona por su ID
def delete_person(person_lname):
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM people WHERE lname = ?', (person_lname,))
        conn.commit()  # Confirma los cambios en la base de datos
    finally:
        cursor.close()
        conn.close()

