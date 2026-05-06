seriesList = ["GOT", "AOT", "TMNT", "TBATE"]

'''
for serie in seriesList:
    if serie == "TMNT":
        break
    print(serie)

for serie in seriesList:
    if serie == "TMNT":
        continue
    print(serie)
'''

name = input("Digite o nome do filme: ")
qntdRatings = int(input("Quantas pessoas avaliarão o filme: "))

total = 0
for i in range(qntdRatings):
    rating = float(input(f"Digite a nota {i+1}: "))
    total += rating

if qntdRatings > 0:
    average = total / qntdRatings
else:
    average = 0

print(f"Média de avaliação do filme {name} é: {average:.2f}")