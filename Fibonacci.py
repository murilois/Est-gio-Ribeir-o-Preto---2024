numero = int(input("Insira um número: "))
fib_sequence = [0, 1]
while fib_sequence[-1] <= numero:
    proximonumero = fib_sequence[-1] + fib_sequence[-2]  
    fib_sequence.append(proximonumero)  
if numero in fib_sequence:
    print(f"{numero} está na sequência!")
else:
    print(f"{numero}não está na sequência!")