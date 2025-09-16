class retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return (f"A área do retângulo é de {area} m².")
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return (f"O perímetro do retângulo é de {perimetro} m.")
    
retangulo01 = retangulo(5, 10)
retangulo02 = retangulo(7, 3)

print(retangulo01.calcular_area())
print(retangulo01.calcular_perimetro())