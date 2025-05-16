import os
try:

    def cadastrar_notas(num):
        for i in range(num):
            nome = input('Informe o nome do aluno: ')
            nota = float(input('Informe a nota do teste: '))
            nota2 = float(input('Informe a nota da prova: '))

            if not (0 <= nota <= 10) or not (0 <= nota2 <= 10):
                raise ValueError('As notas devem estar entre 0 e 10')

            aluno = {
                'Nome': nome,
                'Nota_1': nota,
                'Nota_2': nota2,
                'Media': 0.0,
                'Resultado': ''
            }

            lst_boletim.append(aluno)

    lst_boletim = []

    turma = input('Qual é a turma: ')
    num = int(input('Desaja cadastrar quantas notas? '))
    cadastrar_notas(num)

except Exception as e:
    print(f'Erro, -  {e}\n')

else:
    os.system('cls')
    print(f'==================== Boletim escolar turma: {turma} ==========================')
    for aluno in lst_boletim:
        media = (aluno['Nota_1'] + aluno['Nota_2'])/2
        aluno['Media'] = media
        if media >= 6:
            aluno['Resultado'] = 'Aprovado'
        else:
            aluno['Resultado'] = 'Reprovado'

        print(f"\nNome: {aluno['Nome']}, Média: {aluno['Media']:.2f}, Resultado: {aluno['Resultado']}")

finally:
    print('==========================================================================')
