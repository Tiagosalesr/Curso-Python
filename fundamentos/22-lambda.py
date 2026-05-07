power = lambda num: num ** 2

print(power(5))

par = lambda num: num % 2 == 0

print(par(30))

divide = lambda num1, num2: num1/num2

print(divide(30,15))

seriesList = ["GOT", "AOT", "TMNT", "TBATE"]
ratings = {
    "GOT": [8.9,3,3],
    "AOT": [9.99,4,4],
    "TMNT": [8.56,9,9],
    "TBATE": [5.6, 8 ,8]
}

average_rating = lambda serie_name: sum(ratings[serie_name]) / len(ratings[serie_name])

print(average_rating("GOT"))