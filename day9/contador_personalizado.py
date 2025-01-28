# Contador que conta até o número especificado pelo usuário
def contador():
    try:
        limite = int(input("Escolha o limite da contagem: "))
        for i in range(limite + 1):
            print (i)
            if i == limite:
                print("Chegou ao limite")
                break
    except ValueError:
        print("Entrada inválida. Por favor insira um número inteiro")

contador()