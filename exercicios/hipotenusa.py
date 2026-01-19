# Faça um programa que receba o valor dos catetos de um triângulo,
# calcule e mostre o valor da hipotenusa

c1 = float(input("Insira o valor do primeiro cateto: "))
c2 = float(input("Insira o valor do segundo cateto: "))

hipotenusa = (c1 ** 2 + c2 ** 2) ** (1/2)

print(f"Valor da hipotenusa: {hipotenusa}")