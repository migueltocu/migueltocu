# 2. Ejercicios Sesión 2
#   1. Crea una aplicación de consola que calcule los resultados de una inversión. Debe:
#   2. Pedir por consola una cantidad (numérica) de Inversión
#   3. Pedir el % de interés anual
#   4. Pedir el número de años que se va a mantener la inversión
#   5. Finalmente, calcular la cantidad generada en los años especificados por el usuario



print("Hola. Bienvenido al sistema de cálculo de inversiones")
print("¿Cuánto quieres invertir?")
capital_inicial = input("")
print("¿Cuál es el interés anual?")
interes_anual = input("")
print("¿Cuántos años vas a mantener la inversión?")
años = input("")

#Tengo que averiguar la forma de que los datos de input sean int y float y no string.
capital_final = capital_inicial * (1 + interes_anual) ** (años)
interes_generado = capital_final - capital_inicial

print(f"En {años} años habrás generado {interes_generado}€ de interés")
