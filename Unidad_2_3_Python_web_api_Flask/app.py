from flask import Flask, render_template
from flask_restx import Api, Resource, fields
from people import read_all, create_person, get_person_by_lname, delete_person, update_person

# Configuración de la aplicación Flask
app = Flask(__name__, template_folder='Templates')  # Creamos una instancia de Flask y especificamos la carpeta de plantillas

# Configuración de la API REST con Flask-RESTX
api = Api(app, version='1.0', title='Mi API',  # Creamos una instancia de Api para nuestra API REST
          description='Una API simple', doc='/api/people')  # Especificamos la descripción y ruta de la documentación de Swagger

# Namespace para organizar los recursos de la API
ns = api.namespace('people', description='Operaciones con personas', path='/api/people') # Creamos un espacio de nombres para agrupar los recursos relacionados con personas

# Definición del modelo de datos para una persona
person_model = api.model('Person', {  # Creamos un modelo para representar los datos de una persona
    'id': fields.String(required=True, description='ID'),  # Campo obligatorio para la id
    'fname': fields.String(required=True, description='Nombre'),  # Campo obligatorio para el nombre
    'lname': fields.String(required=True, description='Apellido'),  # Campo obligatorio para el apellido
    'timestamp': fields.String(description='Marca de tiempo')  # Campo opcional para registrar la fecha y hora
})

# Ruta para la página de inicio (HTML)
@app.route('/home')  # Decorador para definir la ruta "/home"
def home():
    return render_template('home.html')  # Renderizamos la plantilla "home.html" cuando se accede a "/home"

# Recurso para listar y crear personas (API REST)
@ns.route('/')
class PersonList(Resource):
    '''Muestra una lista de todas las personas y permite agregar nuevas personas mediante POST.'''

    @ns.doc('list_people')  # Documentación para Swagger
    @ns.marshal_list_with(person_model)  # Especifica el formato de salida (lista de personas según el modelo)
    def get(self):
        '''Lista todas las personas.'''
        return read_all()  # Llamamos a la función read_all() para obtener la lista de personas

    @ns.doc('create_person')  # Documentación para Swagger
    @ns.expect(person_model)  # Especifica el formato de entrada (datos de una persona según el modelo)
    @ns.marshal_with(person_model, code=201)  # Especifica el formato de salida y código de estado (201 Created)
    def post(self):
        '''Crea una nueva persona.'''
        new_person = api.payload  # Obtenemos los datos de la nueva persona del cuerpo de la solicitud
        created_person = create_person(new_person['id'], new_person['fname'], new_person['lname'])  # Llamamos a la función create_person() para crear la persona
        return created_person, 201  # Retornamos los datos de la persona creada y el código de estado 201

# Recurso para obtener, actualizar o eliminar una persona (API REST)
@ns.route('/<string:lname>')
@ns.response(404, 'Person not found')
@ns.param('lname', 'El identificador de la persona (apellido)')  # Documentación del parámetro
class Person(Resource):
    '''Muestra los datos de una persona y permite eliminarla.'''

    @ns.doc('get_person')  # Documentación para Swagger
    @ns.marshal_with(person_model)  # Especifica el formato de salida (datos de una persona según el modelo)
    def get(self, lname):
        '''Obtiene los datos de una persona por su apellido.'''
        person = get_person_by_lname(lname)  # Buscamos a la persona por su apellido
        if person: 
            return person  # Retornamos los datos de la persona si se encuentra
        api.abort(404)  # Si no se encuentra, lanzamos un error 404

    @ns.doc('delete_person')  # Documentación para Swagger
    @ns.response(204, 'Person deleted') 
    def delete(self, lname):
        '''Elimina a una persona por su apellido.'''
        success = delete_person(lname)  # Intentamos eliminar a la persona
        if success:
            return '', 204  # Retornamos una respuesta vacía con código de estado 204 si se eliminó correctamente
        api.abort(404)  # Si no se encuentra, lanzamos un error 404

    @ns.expect(person_model)  # Especifica el formato de entrada (datos de una persona según el modelo)
    @ns.marshal_with(person_model)  # Especifica el formato de salida (datos de una persona según el modelo)
    def put(self, lname):
        '''Actualiza los datos de una persona por su apellido.'''
        updated_person = update_person(lname, api.payload)  # Intentamos actualizar a la persona
        if updated_person:
            return updated_person  # Retornamos los datos actualizados de la persona si se encuentra
        api.abort(404)  # Si no se encuentra, lanzamos un error 404
 
# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)  # Iniciamos la aplicación en modo debug, escuchando en todas las interfaces de red (0.0.0.0) en el puerto 8000
