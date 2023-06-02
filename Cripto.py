# Desenvolva uma classe base chamada Criptografia que contenha os métodos cifrar e decifrar. Essa
# classe servirá como base para as subclasses CifraCesar e CifraXor, que implementarão algoritmos
# de criptografia específicos.
# A classe Criptografia terá os seguintes métodos:
# • Método cifrar(texto): Este método receberá um texto como entrada e retornará o texto
# cifrado de acordo com o algoritmo de criptografia. Cada subclasse irá implementar sua
# própria lógica de cifragem.
# • Método decifrar(texto_cifrado): Este método receberá um texto cifrado como entrada e
# retornará o texto original decifrado de acordo com o algoritmo de criptografia
# correspondente.
# A classe CifraCesar herda da classe Criptografia e implementa o algoritmo de criptografia conhecido
# como Cifra de César. A Cifra de César desloca cada letra do texto original um número fixo de posições
# no alfabeto para cifrar e decifrar o texto.
# A classe CifraXor herda da classe Criptografia e implementa o algoritmo de criptografia usando a
# operação XOR (OU exclusivo). Nesse algoritmo, cada caractere do texto original é combinado com uma
# chave usando a operação XOR para obter o texto cifrado. A operação XOR também é usada para decifrar
# o texto cifrado, combinando-o novamente com a mesma chave.
# Os métodos cifrar e decifrar de cada subclasse devem ser implementados de acordo com a lógica
# específica de cada algoritmo de criptografia.
class Criptografia:
    def cifrar(self, texto):
        pass
    
    def decifrar(self, texto_cifrado):
        pass


class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento
    
    def cifrar(self, texto):
        texto_cifrado = ""
        for caractere in texto:
            if caractere.isalpha():
                codigo = ord(caractere)
                codigo = (codigo - 97 + self.deslocamento) % 26 + 97
                texto_cifrado += chr(codigo)
            else:
                texto_cifrado += caractere
        return texto_cifrado
    
    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for caractere in texto_cifrado:
            if caractere.isalpha():
                codigo = ord(caractere)
                codigo = (codigo - 97 - self.deslocamento) % 26 + 97
                texto_decifrado += chr(codigo)
            else:
                texto_decifrado += caractere
        return texto_decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave
    
    def cifrar(self, texto):
        texto_cifrado = ""
        for caractere in texto:
            codigo = ord(caractere)
            codigo ^= self.chave
            texto_cifrado += chr(codigo)
        return texto_cifrado
    
    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for caractere in texto_cifrado:
            codigo = ord(caractere)
            codigo ^= self.chave
            texto_decifrado += chr(codigo)
        return texto_decifrado


# Exemplo de uso:
texto_original = "Exemplo de texto original"
cifra_cesar = CifraCesar(3)
texto_cifrado = cifra_cesar.cifrar(texto_original)
texto_decifrado = cifra_cesar.decifrar(texto_cifrado)

print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)


cifra_xor = CifraXor(1)
texto_cifrado = cifra_xor.cifrar(texto_original)
texto_decifrado = cifra_xor.decifrar(texto_cifrado)


print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
print("Texto decifrado:", texto_decifrado)