def idade_dirigir(idade):
    if idade >= 18:
        return "Possui idade suficiente para dirigir"
    else:
        return "Não possui idade suficiente para dirigir"

try: 
    idade = int(input("Qual a sua idade: "))
    print(idade_dirigir(idade))
except ValueError:
    print("Entrada invalida. Por favor coloque uma idade válida!")
    