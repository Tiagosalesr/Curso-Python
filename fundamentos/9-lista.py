name = input("Nome do filme:")
releaseYear = int(input("Ano de lançamento: "))
rankMovie = float(input("Nota do filme: "))
planIncluded = True

filme = [name, releaseYear , rankMovie, planIncluded]
print(filme[:2])
print(len(filme))
