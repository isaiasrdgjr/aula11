print('==== CAIXA ELETRÔNICO ====')

try:
    saldo = 1000
    saque = float(input('Informe o valor do saque: '))

except ValueError as e:
    print(f'Erro, digite número - {e}\n')

else:
    if saque <= saldo and saque > 0:
        print(f'Saque autorizado: R${saque}\n')
        saldo -= saque
        print(f'Saldo atual de: R${saldo:.2f}\n')
    elif saque <= 0:
        print('O saque precisa ser maior que zero\n')
    else:
        print('Sem saldo para o saque \n')
finally:
    print('Fim da operação.')
