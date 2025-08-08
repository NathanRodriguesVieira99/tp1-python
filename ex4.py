ANO_2_digitos = 7
tempo_minutos = 150 + ANO_2_digitos
tempo_horas = 2.25

horas_equivalentes = tempo_minutos / 60
minutos_equivalentes = tempo_horas * 60

print(f"Tempo em minutos: {tempo_minutos}")
print(f"Convertido para horas: {horas_equivalentes:.2f}")
print()
print(f"Tempo em horas: {tempo_horas}")
print(f"Convertido para minutos: {minutos_equivalentes}")
