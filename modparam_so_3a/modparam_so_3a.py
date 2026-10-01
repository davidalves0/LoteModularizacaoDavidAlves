
from modparam_so_3a.so_3a_modulo.so_3a_modulo import LoFatorial

if __name__ == "__main__":
    numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
    resultado = LoFatorial.calcularfatorialdasilva(numero)
    print(f"O fatorial de {numero} é: {resultado}")