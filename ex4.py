def ex4():
    saldo = 0
    meses = 0
    investido = 0
    investimento_mensal = 500
    rendimento_mensal = 0.0005
    marco_100k = None
    valores_dolar = [4.95, 5.02, 5.10, 5.20, 5.18, 5.25, 5.30, 5.40, 5.35, 5.45, 5.50, 5.60]

    
    while saldo < 1000000:
        saldo += investimento_mensal
        investido += investimento_mensal
        saldo = saldo * (1 + rendimento_mensal)
        meses += 1
        
        if saldo >= 100000 and marco_100k is None:
            marco_100k = (meses, investido, saldo - investido)
    
    anos = meses // 12
    meses_restantes = meses % 12
    


    print("\n===========- R$100 mil -===========")
    print("Tempo gasto até R$100 mil:", marco_100k[0] // 12, "anos e", marco_100k[0] % 12, "meses")
    print("Investido até R$100 mil:", "R$", round(marco_100k[1], 2))
    print("Juros até R$100 mil:", "R$", round(marco_100k[2], 2))
    print("\n===========- R$1 milhão -===========")
    print("Tempo até R$1 milhão:", anos, "anos e", meses_restantes, "meses")
    print("Total investido:", "R$", round(investido, 2))
    print("Juros totais:", "R$", round(saldo - investido, 2))
    print("Saldo final:", "R$", round(saldo, 2))
    

ex4()