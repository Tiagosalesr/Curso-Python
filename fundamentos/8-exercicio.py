firstName = input("Digite seu nome: ")
lastName = input("Digite o último nome: ")
nome = f"{lastName}, {firstName}"
print(nome)

inverter = "Subi no Onibus"
palavras = inverter.split()
invertido = " ".join(palavras[::-1])

print(invertido)

if inverter[::-1].lower().replace(" ", "") == inverter.lower().replace(" ", "") : print("É palíndromo.") 



