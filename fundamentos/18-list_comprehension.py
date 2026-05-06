listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

seriesList = ["GOT", "AOT", "TMNT", "TBATE"]

moviesWithA = [serie for serie in seriesList if 'o' in serie.lower()]
print(moviesWithA)

while True:
    searchName = input("Digite o nome da série para buscar na lista (ou 'sair' para encerrar):\n")
    if searchName.lower() == "sair":
        print("Programa Encerrado")
        break
    
    findSerie = [serie for serie in seriesList if searchName.lower() in serie.lower()]
    if findSerie:
        print(f"Série encontrada com o nome: {findSerie}: ")
        for foundSerie in findSerie:
            print(foundSerie)
    else:
        print(f"Nenhuma série foi encontrado.")
    