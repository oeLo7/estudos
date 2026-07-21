nome = input("Qual é seu nome? ")
print(f"Olá {nome:>20}!")
print(f"Olá {nome:^20}!")
print(f"Olá {nome:=^20}!")

print("")

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f"A soma é {s}, \n a multiplicação é {m}, a divisão é {d:.3f}", end=" ")
print(f"Divisão inteira é {di} e a exponênciação é {e}")
