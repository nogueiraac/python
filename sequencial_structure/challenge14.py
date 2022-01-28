peso_pescado = float(input("Informe o peso pescado: "))

if peso_pescado > 50:
    excesso = peso_pescado - 50
else: 
    excesso = 0

multa = excesso * 4

print("Multa a ser paga em R$:", multa)