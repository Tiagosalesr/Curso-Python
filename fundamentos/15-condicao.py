name = input("Digite o nome do filme: ")
releaseYear = int(input("Ano de lançamento: "))
rating = float(input("Nota: "))

filme = {
    "Nome": name,
    "Lancamento": releaseYear,
    "Avaliacao": rating
}

if filme["Avaliacao"] > 8.0 and releaseYear > 2015:
    print(f"O filme {filme['Nome']} é recomendado")
else: 
    print(f"O filme {filme['Nome']} não é recomendado")