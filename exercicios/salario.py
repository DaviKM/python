# Faça um programa que recebe o salário de um funcionário e o percentual de aumento,
# calcule e mostre o valor do aumento e o novo salário.

sal_atual = float(input("Insira o salário atual: "))
per_aumento = float(input("Insira o percentual de aumento: "))

novo_sal = sal_atual + sal_atual*per_aumento/100

print(f"Novo salário: {novo_sal}")