import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""
    
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Generador seguro de contraseñas
print("=== Generador Seguro de Contraseñas ===")

opcion = input("¿Desea generar una contraseña? (si/no): ").lower()

if opcion == 'si':
    longitud = int(input("Longitud de la contraseña (mínimo 8): "))

    if longitud < 8:
        print("La longitud mínima recomendada es 8 caracteres.")
    else:
        usar_mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
        usar_minusculas = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
        usar_numeros = input("¿Incluir números? (si/no): ").lower() == 'si'
        usar_simbolos = input("¿Incluir símbolos? (si/no): ").lower() == 'si'

        contraseña = generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos)
        print("\nContraseña generada:")
        print(contraseña)
else:
    print("Saliendo del programa...")
    