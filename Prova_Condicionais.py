# Prova Condicionais

velocidade = float(input("Qual é a velocidade do carro em km/h? "))


limite_velocidade = 80
valor_multa_por_km = 20

if velocidade > limite_velocidade:
    excesso_velocidade = velocidade - limite_velocidade
    valor_multa = excesso_velocidade * valor_multa_por_km

    print(f"Você foi multado, exesso de velocidade! O valor da multa é R${valor_multa:.2f}.")

else:
    print("Você esta dentro do limite de velocidade. Não sera multado.")
