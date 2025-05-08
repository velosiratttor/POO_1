Animales = ["Gato", "perro","lora","gaviota"]
edades = [12,25,30,4]
edad1 = 0
edad2 = 4

#
for animal in Animales: 
    print(animal)
    

#RECORRER LISTA 

for animal in Animales:
    print(f"Ahora la variable de animal es : {animal}")
    
#RECORRER LISTA MODIFICADA

for edad in edades :
    Resultado = edad*2
    print(f"las edades son : {Resultado}")
    
#RECORRER MAS DE UNA LISTA EN UN SOLO FOR 

for animal , edad in zip(Animales,edades):
    print(edad)
    print(animal)
    
    
#RECORRER UNA LISTA CON RANGE

for num in range (0,5):
    print(num)
    
#RECORRER LISTA CON INDICES 

for num in enumerate (edades):
    print(num)
    
#USANDO EL ELSE CON FOR 

for num in edades:
    print(num)
else:
    print("simulacro terminado") 
    
Datos = {
    "Nombre" : "Samuel",
    "Apellido" : "Chavarria",
    "Edad" : 20
}

print(Datos)

#RECORRIENDO DICCIONARIO 

for key in Datos.items():
    print(key)
    
#ITERAR OTROS DAROS DE OTRA FORMA 

for key in Datos.items():
    kei = [0]
    Value = [1]
    print(f"La llave es: {kei} y el valor es {Value}")
    
    
edadess = [1,3,5,12]
Frutas = ["Vejetal", "Naranja", "Melon"]
nombres = "Hi mi nombre es Samuel"

for ed in edadess :
    if ed==3:
        continue
    print(ed)
    
for ed in edadess : 
    if ed == 3 :
        break
    print(ed)
else:
    print("Simulacro terminado")
    
#ITERANDO UNA CADENA 

for cadena in nombres :
        print (cadena)
        
#FOR EN UNA SOLA LINEA DE CODIGO (DUPLICADO, VALORES)

numeros_duplicado = [x*2 for x in edadess]
print(numeros_duplicado)

frutas = ["Melon", "Manzanas", "Naranjas"]
i = 0

while i< len (frutas):
    print(frutas[i])
    i += 1
    

contador = 0 

while contador < 5 :
    print (contador)
    contador+=1