km_por_dia = 19
ANO_2_digitos = 7
gasto_diario = 300 + ANO_2_digitos

print("--- CÁLCULOS  ---")
print(f"Quilômetros por dia: {km_por_dia} km")
print(f"Gasto diário: R$ {gasto_diario}")
print()

print("--- RESULTADOS ---")

total_semana = km_por_dia * 7
print(f"1. Total em uma semana: {total_semana} km")

diferenca = 100 - gasto_diario
print(f"2. Diferença entre R$100 e gasto diário: R$ {diferenca}")

dias_cobertura = 500 // gasto_diario
print(f"3. Quantos dias R$500 cobre: {dias_cobertura} dias")

resto = gasto_diario % 100
print(f"4. Resto da divisão do gasto diário por 100: {resto}")

custo_por_km = gasto_diario / km_por_dia
print(f"5. Custo por km: R$ {custo_por_km:.2f}")
