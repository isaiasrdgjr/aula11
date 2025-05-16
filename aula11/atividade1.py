try:
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))

except ValueError as e:
     print(f'Erro, valor da variável deve ser numérico - {e}')

else:
     if(nota1 and nota2 >= 0) and (nota1 and nota2 <= 10):
            media = (nota1+nota2)/2
            if media >= 6:
                  print(f'O aluno foi aprovado! A média foi {media:.2f}')
     else:
           print('As notas estão fora do intervalo de 0 a 10')           
     
finally:
    print('Fim da execução do programa.')
