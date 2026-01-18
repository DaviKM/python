tipo = input("Insira o tipo do triângulo (A ou B): ").upper()
while tipo != "A" and tipo != "B":
    tipo = input("Erro! Insira um valor válido (A ou B): ").upper()

tamanho = int(input("Insira o tamanho do triângulo: "))

i = 0


if tipo == "A" :
    while i < tamanho:
        j = 0
        while j < i + 1:
            print("*", end="")
            j += 1
        i += 1
        print("\n", end="")