import sys
sys.setrecursionlimit(3000)
def investir_em_bitcoin(saldo_bitcoins=0, mes_atual=0, total_aplicado=0, metas_alcancadas=None):
    if metas_alcancadas is None:
        metas_alcancadas = set()

    valor_bitcoin = 664484 # preço do bitcóio
    cotações_bitcoin = [209410, 212335, 306600, 359693, 316517, 355299, 352500, 368540, 333842, 345411, 409131, 580819]
    valor_investido_por_mes = 250
    rendimento_diario = 0.0005
    metas_de_valor = {100000, 1000000, valor_bitcoin}

    cotacao_do_mes = cotações_bitcoin[mes_atual % 12]
    quantidade_bitcoins_comprados = valor_investido_por_mes / cotacao_do_mes
    saldo_bitcoins *= (1 + rendimento_diario) 
    saldo_bitcoins += quantidade_bitcoins_comprados
    total_aplicado += valor_investido_por_mes
    mes_atual += 1

    saldo_em_reais = saldo_bitcoins * cotacao_do_mes

    for meta in metas_de_valor - metas_alcancadas:
        if saldo_em_reais >= meta:
            anos_passados = mes_atual // 12
            meses_faltando = mes_atual % 12
            ganhos_com_juros = saldo_em_reais - total_aplicado

            # olha que beleza de print
            if meta == 100000:
                print("\n===========- R$100 mil -===========")
                print("Tempo gasto até R$100 mil:", anos_passados, "anos e", meses_faltando, "meses")
                print("Investido até R$100 mil:", "R$", round(total_aplicado, 2))
                print("Juros até R$100 mil:", "R$", round(ganhos_com_juros, 2))

            if meta == 1000000:
                print("\n===========- R$1 milhão -===========")
                print("Tempo até R$1 milhão:", anos_passados, "anos e", meses_faltando, "meses")
                print("Total investido:", "R$", round(total_aplicado, 2))
                print("Juros totais:", "R$", round(ganhos_com_juros, 2))
                print("Saldo final:", "R$", round(saldo_em_reais, 2))

            metas_alcancadas.add(meta)

    if metas_alcancadas != metas_de_valor:
        return investir_em_bitcoin(saldo_bitcoins, mes_atual, total_aplicado, metas_alcancadas)

print("")
print(".==================================================.")
investir_em_bitcoin()

