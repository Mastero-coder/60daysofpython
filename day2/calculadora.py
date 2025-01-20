def soma(number1, number2):
    return number1 + number2

def mutiplicação(number1, number2):
    return number1 * number2

def divisão(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        print("Não existe operação por zero!")

def subtração(number1, number2):
    return number1 - number2 

while True:
    escolha = input("Deseja iniciar? ")

    if escolha == "não":
        print("Progama finalizado!")
        break

    number1 = int(input("Escreva do primeiro número: "))
    number2 = int(input("Escreva o segundo número: "))

    operation = input("Qual operação você deseja realizar: ")

    if operation == "soma":
        result = soma(number1, number2)

    elif operation == "multiplicação":
        result = mutiplicação(number1, number2)

    elif operation == "divisão":
        if number2 != 0:
            result = divisão(number1, number2)
        else:
            print("Não existe operação de divisão por zero!")

    elif operation == "subtração":
        result = subtração(number1, number2)

    else:
        print("Operação inválida!")

    print(f"A operação de {operation} dos números {number1} e {number2} é igual {result}")
    print("-" * 50)