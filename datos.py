from datetime import datetime

# Datos personales del usuario
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
mail = input("Ingrese su correo: ")
sexo = input("Ingrese su sexo: ")
phone = input("Ingrese su numero de telefono: ")

print("\n--- Fecha de Nacimiento ---")
day = int(input("Ingrese el día de nacimiento (DD): "))
month = int(input("Ingrese el mes de nacimiento (MM): "))
birthyear = int(input("Ingrese el año de nacimiento (YYYY): "))

# Obtener la fecha actual (Año: 2026)
fecha_actual = datetime.now()

# Calcular la edad inicial restando los años
age = fecha_actual.year - birthyear

# COMPROBADOR: Verificar si ya cumplió años este año
# Si el mes actual es menor al mes de nacimiento, O si es el mismo mes pero el día actual es menor, aún no cumple años.
if (fecha_actual.month, fecha_actual.day) < (month, day):
    age -= 1  # Se le resta un año porque no ha llegado su cumpleaños
    cumplio_este_anio = "No"
else:
    cumplio_este_anio = "Sí"

# Mostrar resultados
print("\n--- Resumen de Datos ---")
print(f"Nombre: {name}")
print(f"Apellido: {lastname}")
print(f"Correo: {mail}")
print(f"Sexo: {sexo}")
print(f"Telefono: {phone}")
print(f"Fecha de Nacimiento: {day}/{month}/{birthyear}")
print(f"Edad Exacta: {age} años")
print(f"¿Ya cumplió años este año?: {cumplio_este_anio}")