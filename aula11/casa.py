def cadastrar_notas(num):
    for i in range(num):
        nome = input('Informe o nome do aluno: ')
        nota = float(input('Informe a nota: '))
        nota2 = float(input('Informe a nota: '))

        aluno = {
            'Nome': nome,
            'Nota_1': nota,
            'Nota_2': nota2
        }

        lst_boletim.append(aluno)


def calcula_total_media():
    tot = 0
    for aluno in lst_boletim:
        tot = aluno['Nota_1'] + aluno['Valor_2']
    med = tot/2
    return med

def cadastrar_notas(num):
    for i in range(num):
        nome = input('Informe o nome do aluno: ')
        nota = float(input('Informe a nota: '))
        nota2 = float(input('Informe a nota: '))

        aluno = {
            'Nome': nome,
            'Media': nota
        }

        lst_boletim.append(aluno)


lst_boletim = []
lst_boletim_final = []
num = int(input('Desaja cadastrar quantas notas? '))
cadastrar_notas(num)
