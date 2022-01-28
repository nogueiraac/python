ganho_por_hora = float(input("Digite o quanto você ganha por hora trabalhada: "))
numero_horas_trab_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = ganho_por_hora * numero_horas_trab_mes

salario_pos_imposto = salario_bruto - ((salario_bruto/100) * 11) 
diff_imposto = salario_bruto - salario_pos_imposto

salario_pos_inss = salario_pos_imposto - ((salario_pos_imposto/100) * 8)
diff_inss = salario_pos_imposto - salario_pos_inss


salario_pos_sindicato = salario_pos_inss - ((salario_pos_inss/100) * 5)
diff_sindicato = salario_pos_inss - salario_pos_sindicato


print("Salário Bruto em R$: ", salario_bruto)

print("\nQuanto pagou ao INSS em R$: ", diff_inss)

print("\nQuanto pagou ao Sindicato em R$: ", diff_sindicato)

print("\nSalário Líquido em R$: ", salario_pos_sindicato)
