def welcome():
    print("Bem vindo ao sistema!")

welcome()

def average(num1, num2):
    media = (num1 + num2)/2
    return media

print(average(2,2))

def full_name(firstName, lastName):
    return f"{lastName}, {firstName}"

print(full_name("Tiago", "Ribeiro"))

#parâmetro default

def adress(country="Brasil"):
    print(f"Eu moro em {country}")

adress()