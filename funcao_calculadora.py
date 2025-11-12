def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2

    if operacao == '-':
        return numero1 - numero2

    if operacao == '*':
        return numero1 * numero2

    if operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero"

    return "Operação invalida"

# ex

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))
resultado = calculadora(numero1, numero2, operacao)

print("Resultado:", resultado)
