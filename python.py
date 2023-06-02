# 2. Crie uma classe base chamada Veiculo com os seguintes atributos:
# • marca: marca do veículo (string)
# • modelo: modelo do veículo (string)
# • ano: ano de fabricação do veículo (int)
# A classe Veiculo deve ter os seguintes métodos:
# • acelerar(): exibe a mensagem "Acelerando o veículo!"
# • frear(): exibe a mensagem "Freando o veículo!"
# Crie três classes derivadas da classe Veiculo:
# • Carro: com os atributos adicionais:
# • cor: cor do carro (string) 
#   A classe Carro deve ter os seguintes métodos adicionais:
# • ligar_radio(): exibe a mensagem "Ligando o rádio do carro!"
# • abrir_porta(): exibe a mensagem "Abrindo a porta do carro!"
# • Moto: com os atributos adicionais:
# • cilindrada: cilindrada da moto (string) A classe Moto deve ter os seguintes métodos
# adicionais:
# • empinar(): exibe a mensagem "Empinando a moto!"
# • buzinar(): exibe a mensagem "Buzinando a moto!"
# • Caminhao: com os atributos adicionais:
# • carga_maxima: capacidade máxima de carga do caminhão (string) A classe
# Caminhao deve ter os seguintes métodos adicionais:
# • carregar(): exibe a mensagem "Carregando o caminhão!"
# • descarregar(): exibe a mensagem "Descarregando o caminhão!"

class Veiculo:
    def __init__(self,marca,modelo,fabricacao,):
        self._marca=marca
        self._modelo=modelo
        self._fabricacao=fabricacao

    def acelerar(self):
        print(self._modelo,'da',self._marca,'está acelerando')
    def frear(self):
        print(self._modelo,'da',self._marca,'está freiando')  
      
class Carro(Veiculo):
    def __init__(self,marca,modelo,fabricacao,cor):
        super().__init__(marca,modelo,fabricacao)
        self._cor=cor
    
    def ligar_radio(self):
        print(self._modelo,'da',self._marca,'Ligou o rádio')
    
    def abrir_porta(self):
        print(self._modelo,'da',self._marca,'Abriu a porta')

class Moto(Veiculo):
    def __init__(self,marca,modelo,fabricacao,cilindrada):
        super().__init__(marca,modelo,fabricacao)
        self._cilindrada=cilindrada
    
    def empinar(self):
        print(self._modelo,'da',self._marca,'está empinando')
    
    def buzinar(self):
        print(self._modelo,'da',self._marca,'está buzinando')

class Caminhao(Veiculo):
    def __init__(self,marca,modelo,fabricacao,carga_maxima):
        super().__init__(marca,modelo,fabricacao)
        self._carga_maxima=carga_maxima
    
    def carregar(self):
        print(self._modelo,'da',self._marca,'está sendo carregado')
    
    def descarregar(self):
        print(self._modelo,'da',self._marca,'está sendo descarregado')

carro=Carro('VW','Gol',2006,'vermelho')
moto=Moto('Honda','CG',2008,'125')
caminhao=Caminhao('VW','Cargo',2018,'12000kg')

carro.acelerar()
carro.frear()
carro.abrir_porta()
carro.ligar_radio()
print()
moto.acelerar()
moto.frear()
moto.empinar()
moto.buzinar()
print()
caminhao.acelerar()
caminhao.frear()
caminhao.carregar()
caminhao.descarregar()