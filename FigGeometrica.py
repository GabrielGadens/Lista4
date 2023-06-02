class FiguraGeometrica:
    def __init__(self, nome):
        self.nome = nome
    

# Classe derivada
class Retangulo(FiguraGeometrica):
    def __init__(self, nome,base,altura):
        super().__init__(nome)
        self.__base=base
        self.__altura=altura
    def calcularArea(self):
        area=self.__base*self.__altura
        return area
    
    def calcularPerimetro(self):
        per=((self.__altura+self.__base)*2)
        return per
        
class Triangulo(FiguraGeometrica):
    def __init__(self, nome,base,altura,l1,l2): 
        super().__init__(nome) 
        self.__base=base
        self.__altura=altura
        self.__l1=l1
        self.__l2=l2
    def calcularArea(self):
        area=(self.__base*self.__altura)/2
        return area
    def calcularPerimetro(self):
        per = self.__l1+self.__l2+self.__base
        return per

class Circulo(FiguraGeometrica):
    def __init__(self, nome,raio): 
        super().__init__(nome) 
        self.__raio=raio
    def calcularArea(self):
        area = (self.__raio*self.__raio)*3.14159265359
        return area
    def calcularCircun(self):
        circun = (self.__raio*2)*3.14159265359
        return circun

circulo=Circulo('piscina',5)
triangulo=Triangulo('piramide',10,6,4,5)
retangulo=Retangulo('caixa',10,20)
print(circulo.calcularArea())
print(circulo.calcularCircun())
print()
print(triangulo.calcularArea())
print(triangulo.calcularPerimetro())
print()
print(retangulo.calcularArea())
print(retangulo.calcularPerimetro())