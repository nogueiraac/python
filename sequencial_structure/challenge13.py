altura = float(input("Insira a altura: "))
sexo = input("Informe o sexo: ")

if sexo == "homem":
    peso_ideal = (72*altura) - 58
elif sexo == "mulher":
    peso_ideal = (62.1*altura) - 44.7

print("Peso ideal seria: ", peso_ideal)