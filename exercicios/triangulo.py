#  Faça um programa que receba três valores, A, B e C, analise estes valores e informe ao usuário
# se estes podem ser os lados de um triângulo. O ABC será um triângulo se cada um dos lados for
# menor que a soma dos outros dois. Obs: Seu algoritmo não deve permitir entrada de valores
# inválidos para as medidas candidatas a lados do triângulo.

a = float(input("Insira o lado A: "))
b = float(input("Insira o lado B: "))
c = float(input("Insira o lado C: "))

if a + b > c and b + c > a and c + a > b:
    print("Estes lados podem formar um triângulo!")
else:
    print("Estes lados NÃO podem formar um triângulo!")