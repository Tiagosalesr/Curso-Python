def sum(*num):
    total = 0
    for i in num:
        total += i
    return total

soma_total = sum(2,3,4,5,6,7,8,9,10,1)


def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("Lista de cursos: ")

presentation(nome="ES", IF="INF", turno="noturno")

