Persona = type('Persona', (), {'nombre': '', 'edad': 0})

juan = Persona()
juan.nombre = 'Juan'
juan.edad = 30

print(juan.nombre)  
print(juan.edad)    
