num = int(input("Digite o número: "))

def fatorial(num):
    if num == 1: return 1
    result = num * fatorial(num-1)
    return result

print(f"O fatorial de {num} é: {fatorial(num)}")