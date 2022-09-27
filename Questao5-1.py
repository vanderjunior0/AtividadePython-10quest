print("DIgite tres números em ordem crescente ")

a, b, c = float(input("Digite o 1° número: ")), float(input("Digite o 2° número: ")), float(input("Digite o 3° número: "))
z = float(input("Digite um número fora dessa ordem: "))

if z<=a<b<c:
    print(f"A ordem decrescente é: {c}, {b}, {a} e {z}")
elif a<=z<b<c:
    print(f"A ordem decrescente é: {c}, {b}, {z} e {a}")
elif a<b<=z<c:
    print(f"A ordem decrescente é: {c}, {z}, {b} e {a}")
else:
    print(f"A ordem decrescente é: {z}, {c}, {b} e {a}")