numero = int(input("Insira um número: "))
fibonacci = [0, 1]
while fibonacci[-1] <= numero:
    proximonumero = fibonacci[-1] + fibonacci[-2]  
    fibonacci.append(proximonumero)  
if numero in fibonacci:
    print(f"{numero} está na sequência!")
else:
    print(f"{numero} não está na sequência!")