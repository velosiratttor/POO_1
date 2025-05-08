class Temperatura:
    def __init__(self, celsius=None, fahrenheit=None):
        if celsius is not None:
            self.celsius = celsius
            self.fahrenheit = celsius * 9/5 + 32
        elif fahrenheit is not None:
            self.fahrenheit = fahrenheit
            self.celsius = (fahrenheit - 32) * 5/9

    def mostrar_en_celsius(self):
        print("Celsius:", self.celsius)

    def mostrar_en_fahrenheit(self):
        print("Fahrenheit:", self.fahrenheit)

temp1 = Temperatura(celsius=25)
temp1.mostrar_en_fahrenheit()

temp2 = Temperatura(fahrenheit=77)
temp2.mostrar_en_celsius()
