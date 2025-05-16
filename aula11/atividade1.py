try:
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))

except ValueError as e:
     print(f'Erro, valor da variável deve ser numérico - {e}')

else:
     if(0 <= nota1 <= 10) and (0 <= nota2 <= 10):
            media = (nota1+nota2)/2
            if media >= 6:
                  print(f'O aluno foi aprovado! A média foi {media:.2f}')
     else:
           print('As notas devem estar entre 0 e 10')          
     
finally:
    print('Fim da execução do programa.')
