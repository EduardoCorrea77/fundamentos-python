def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)

    print(f"Ranking: {ranking}")

    return ranking

pontuacoes = [150, 300, 90, 250, 180]

criar_ranking(pontuacoes)