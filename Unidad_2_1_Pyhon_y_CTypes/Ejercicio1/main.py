import ctypes

# Cargar la biblioteca compartida
# En Linux, usarias
# lib = ctypes.CDLL('./libmylib.so')
# En Windows:
lib = ctypes.CDLL('./mylib.dll')

# Especificar el tipo de retorno y los tipos de argumentos de la función suma
lib.suma.restype = ctypes.c_int
lib.suma.argtypes = [ctypes.c_int, ctypes.c_int]

# Llamar a la función suma
resultado = lib.suma(3, 5)
print(f"El resultado de la suma es: {resultado}")