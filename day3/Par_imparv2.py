print("-" * 50)
entrada = input("Escolha um número: ")
print("-" * 50)

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"O número que você escolheu é par: {numero}")
        print("-" * 50)
    else:
        print(f"O número que você escolheu é ímpar: {numero}")
        print("-" * 50)

except ValueError:
    print(f"O seu número não é inteiro")
    print("-" * 50)