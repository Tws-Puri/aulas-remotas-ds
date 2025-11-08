multiplicador = int(input("Qual será o numero selecionado? "))
resultado = 0

print(f"---tabuada do {multiplicador}---")
for i in range(1, 11):
    resultado = multiplicador * i
    print(f"{multiplicador} x {i} = {resultado}")
