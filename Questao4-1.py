a = int(input('Escreva um número: '))
b = int(input('Escreva um número: '))
c = int(input('Escreva um número: '))

if a > b and b > c:
    print(f'A ordem crescente é {c} , {b} e {a}')
elif b > c and c > a:
    print(f'A ordem crescente é {a} , {c} e {b}')
elif b > a and a > c:
    print(f'A ordem crescente é {c} , {a} e {b}')
elif c > b and b > a:
    print(f'A ordem crescente é {a} , {b} e {c}')
elif a > c and c > b:
    print(f'A ordem crescente é {b} , {c} e {a}')
else:
    print(f'A ordem crescente é {b} , {a} e {c}')
