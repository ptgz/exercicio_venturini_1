def ex6():
    saldo = 0
    meses = 0
    investido = 0
    investimento_mensal = 80
    
    div_marfrig = 0.2983
    div_petrobras = 0.1349
    div_itausa = 0.10
    div_medio = (div_petrobras + div_marfrig + div_itausa) / 3
    div_mensal = div_medio / 12
    
    marco_100k = None
    
    while saldo < 1000000:
        saldo += investimento_mensal
        investido += investimento_mensal
        dividendos = saldo * div_mensal
        saldo += dividendos
        meses += 1
        
        if saldo >= 100000 and marco_100k is None:
            marco_100k = (meses, investido, dividendos)
    
    anos = meses // 12
    meses_restantes = meses % 12
    
    print("\n===========- R$100 mil -===========")
    print("Tempo gasto até R$100 mil:", marco_100k[0] // 12, "anos e", marco_100k[0] % 12, "meses")
    print("Investido até R$100 mil:", "R$", round(marco_100k[1], 2))
    print("Dividendos até R$100 mil:", "R$", round(marco_100k[2], 2))
    print("\n===========- R$1 milhão -===========")
    print("Tempo até R$1 milhão:", anos, "anos e", meses_restantes, "meses")
    print("Total investido:", "R$", round(investido, 2))
    print("Dividendos totais:", "R$", round(saldo - investido, 2))
    print("Saldo final:", "R$", round(saldo, 2))
    
ex6()