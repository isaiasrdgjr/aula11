# try:
#     n1 = float(input('Número: '))
#     n2 = float(input('Número: '))
#     div = n1 / n2
#     print(div)
# except ZeroDivisionError as e:
#     print(f'Erro, não pode dividir por 0 - {e}')

# try:
#     n1 = float(input('Número: '))
#     n2 = float(input('Número: '))
#     div = n1 / n2
#     print(div)

# except ZeroDivisionError as e:
#     print(f'Erro, não pode dividir por 0 - {e}')


# except ValueError as e:
#     print(f'Erro, valor da variável deve ser numérico - {e}')

try:
    n1 = float(input('Número: '))
    n2 = float(input('Número: '))
    div = n1 / n2

except Exception as e:
    print(f'Erro - {e}\n')

else:
    print(div)

finally:
    print('Fim da operação.')
