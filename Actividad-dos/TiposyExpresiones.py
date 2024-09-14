# 1) Conversion de tipos de datos

#Enteros
edad = 20
print(type(edad))

#Decimales
Dinero= 23.3
print(type(Dinero))

#Caracter
Cadena = 'Hola mundo'
print(type(Cadena))

#multilinea
multilinea = """En el silencio de la noche,
las estrellas susurran sueños,
mientras la luna observa,
guardiana de secretos antiguos.

Cada suspiro del viento,
lleva consigo historias perdidas,
y en cada sombra que danza,
se esconden mil melodías."""

print(type(multilinea))

# len()
longitud = len(multilinea)
print(type(longitud))

#sub cadenas
#Obtener los primeros n caracteres de una cadena.
n = 5
primero_n = multilinea[:n]
print("Primeros",n, "Caracteres",primero_n)

#Obtener los caracteres de en medio de una cadena.
medio = multilinea[40:80]
print("Caracteres de en medio (índices 40 a 80):", medio)

# Obtener los últimos n caracteres
ultimos_n = multilinea[-10:]
print("Últimos", n, "caracteres:", ultimos_n)

#Upper()
mayus = multilinea.upper()
print(mayus)

#Lower()
minusculas = multilinea.lower()
print(minusculas)

#multilinea de cadenas de caracteres
cadena_multilinea = """La inteligencia artificial (IA) es un campo de estudio
que se centra en la creación de sistemas capaces de realizar tareas
que normalmente requieren inteligencia humana. Esto incluye
actividades como el aprendizaje, el razonamiento y la resolución
de problemas."""

print("Cadena multilínea de caracteres:")
print(cadena_multilinea)

#Funcion strip
strip= cadena_multilinea.strip()
print("Cadena sin espacios:")
print(f"'{strip}'")

#Función replace().
remplazo = cadena_multilinea.replace("IA", "Inteligencia Artificial")
print(remplazo)

#Función split().

lineas = cadena_multilinea.splitlines()
print("Líneas divididas:")
for i, linea in enumerate(lineas):
    print(f"Línea {i + 1}: '{linea}'")


#Formato de cadenas F-String.
nombre = "Zhamuel"
edad = 20

mensaje = f"{nombre} tiene {edad} años."

print(mensaje)