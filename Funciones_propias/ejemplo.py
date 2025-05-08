def saludar():
      print("hola ¿como estas?")

saludar()


def saludar_2(nombre, genero):
    if genero=='masculino':
           adjetivo= 'papu'
    elif genero == 'femenino':
          adjetivo = 'muchacha'
    else:
          adjetivo = 'especial'
                       
    print(f'Hola mi nombre es: {nombre} y soy {genero} y puedes llamarme {adjetivo}')       
           

saludar_2('jose','masculino')
saludar_2('jose','femenino')
saludar_2('jose', 'f')


def suma_doble(num1,num2):
      return num1+num2

resultado = suma_doble(1,2)
print(resultado)