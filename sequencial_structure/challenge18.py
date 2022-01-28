tam_arq = float(input("Insira o tamanho do arquivo em MB:"))
vel_link = float(input("Insira a velocidade do link em Mbps:"))

vel_link_mb = vel_link / 8

tempo = (tam_arq / vel_link_mb)

print("Tempo estimado de download:", tempo)