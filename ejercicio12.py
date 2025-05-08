#12. Crea una clase 'Animal' con un método 'hablar()' que sea sobrescrito por clases hijas como 'Perro' y 'Gato'.

class animal :
    
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def mostrar(self):
        return f'{self.especie} || {self.edad}'

class perro(animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
        self.especie = especie
        self.edad = edad
        
    def hablar(self):
        return f'El {self.especie} esta ladrando'
class gato(animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
        
    def hablar(self):
        return f'El {self.especie} esta maullando'
    
animal1 = gato('Gato', 12)
print(animal1.hablar())