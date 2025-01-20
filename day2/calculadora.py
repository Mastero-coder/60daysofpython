def soma(number1, number2):
    return number1 + number2

def mutiplicação(number1, number2):
    return number1 * number2

    
def divisao(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Erro! Divisão por zero não é permitida."

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
        result = divisao(number1, number2)

    elif operation == "subtração":
        result = subtração(number1, number2)

    else:
        print("Operação inválida!")

    print(f"A operação de {operation} dos números {number1} e {number2} é igual a {result}")
    print("-" * 50)