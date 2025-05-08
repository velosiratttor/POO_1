# Ejercicios de Python: Bucles For y While
# Ejercicios con FOR:

# 1. Imprimir números del 1 al 20, pero solo los que son pares y mayores que 10.

Numeros = [35,4,5,6,7]

for numero in Numeros:
    if numero > 10 and numero % 2 == 0:
        print(numero)
else:
    print("Error vuelva a intentarlo")
    
#______________________________________________________________________________________

# 2. Recorrer una lista de edades y mostrar cuáles son mayores de edad (>=18) y menores de 25.

edades = [20,18,19,30]

for edad in edades:
    if edad >=18 and edad < 25 :
        print(edad)

#3. Mostrar los nombres de una lista que tengan más de 5 letras y contengan la letra 'a'.

Nombres = ["Samuel","Lazaro","Carla","Sebastian"]

for nombre in Nombres:
    if len(nombre) > 5 and "a" in nombre.lower():
        print(nombre)
        
#4. Imprimir números del 1 al 50, solo si son múltiplos de 3 o de 5.

for n in range(1,50):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
        
#5. Dada una lista de números, imprimir los positivos que sean mayores que 10.

num = list(range(-10,30))

for nu in num :
    if nu > 0 and nu  > 10 :
        print(nu)
        
# 6. Mostrar los colores de una lista que empiecen con la letra 'b' y tengan más de 4 letras.

colores = ["Beige","berengena"]

for color in colores:
    if len(color) > 4 and "b" in color.lower():
        print(color)
        

# 7. Recorrer una lista de precios e imprimir los que sean menores a 100 y mayores a 50


precios = [120,51,80,69,111,1]

for precio in precios :
    if precio < 100 and precio > 50:
        print(precio)
