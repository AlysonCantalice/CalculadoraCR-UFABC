import json
from time import sleep
notas = []
mat = {}
def linhas():
    print('='*40)
linhas()
print(f'{"BEM VINDO A CALCULADORA DE CR":^30}')
while True:
    linhas()
    print('''Escolha a opção desejada: 
    0. Mostrar lista do CR
    1. Adicionar uma matéria
    2. Editar uma matéria
    3. Carregar CR salvo
    4. Salvar CR atual
    5. Encerrar programa''')
    linhas()
    r = input('Escolha: ')
    if r.isnumeric():
        r = int(r)
    while type(r) != int:
        r = input('Inválido! Escolha um item usando um número inteiro: ')
        if r.isnumeric():
            r = int(r)
    linhas()
    if r == 0:
        if len(notas) == 0:
            print('Nenhuma matéria cadastrada!')
        else:
            cm = ch = cr = 0
            print(f'{"cod":>5} {"Matéria":<15} {"Conceito":<5}')
            t = 0
            for c in notas:
                print(f'{notas.index(c):>5} {c["nome"]:<15} {c["nota"]:<5}')
                if c["nota"] == 'A':
                    cm = 4
                elif c["nota"] == 'B':
                    cm = 3
                elif c["nota"] == 'C':
                    cm = 2
                elif c["nota"] == 'D':
                    cm = 1
                else:
                    cm = 0
                cr += (cm * c['carga'])
                ch += c['carga']
                cm = 0
            print(f'Créditos totais: {ch}')
            print(f'\033[31mCR: {(cr/ch):.2f}\033[m')
        linhas()
        input('Aperte alguma tecla para continuar... ')
    elif r == 1:
        while True:
            mat['nome'] = str(input('Nome ou sigla da matéria: '))
            mat['carga'] = int(input('Créditos: '))
            mat['nota'] = str(input('Conceito final obtido (A,B,C,D,F): ')).upper()
            notas.append(mat.copy())
            print(f'{mat["nome"]} foi adicionado com sucesso!')
            mat.clear()
            r = str(input('Deseja adicionar outra? [Y/N]: ')).upper()
            while r not in 'YN':
                r = str(input('Inválido! Deseja adicionar outra? [Y/N]: ')).upper()
            if r == 'N':
                break
    elif r == 2:
        if len(notas) == 0:
            print('Nenhuma matéria para editar!')
        else:
            while True:
                linhas()
                print(f'{"cod":>3} Matéria')
                for c in notas:
                    print(f'{(notas.index(c)):>3} {c["nome"]}')
                r = int(input('Digite o código da matéria que deseja editar: '))
                while r > len(notas)-1 or r < 0:
                    r = int(input('Matéria não encontrada! Digite o código da matéria que deseja editar: '))
                while True: 
                    linhas()
                    print(f'''0. Nome: {notas[r]["nome"]} 
1. Carga: {notas[r]["carga"]} 
2. Conceito: {notas[r]["nota"]}''') 
                    e = int(input('Digite o campo que deseja editar ou 999 para excluir a matéria: '))
                    while e not in [0,1,2,999]:
                        e = int(input('Inválido! Digite o campo que deseja editar ou 999 para excluir a matéria: '))
                    if e == 999:
                        del notas[r]
                        print('Matéria apagada!')
                    elif e == 0:
                        notas[r]["nome"] = str(input('Novo nome: '))
                    elif e == 1:
                            notas[r]["carga"] = int(input('Nova carga: '))
                    elif e == 2:
                            notas[r]["nota"] = str(input('Novo conceito: ')).upper()
                    e = str(input('Deseja continuar editando esta matéria? [Y/N]: ')).upper()
                    while e not in 'YN':
                        e = str(input('Inválido! Deseja continuar editando esta matéria? [Y/N]: ')).upper()
                    if e == 'N':
                        break
                r = str(input('Deseja continuar editando? [Y/N]: ')).upper()
                while r not in 'YN':
                    r = str(input('Inválido! Deseja continuar editando? [Y/N]: ')).upper()
                if r == 'N':
                    break
    elif r == 3: #carregar lista
        print('Carregando',end='')
        for c in range (0,3):
            print('.',end='',flush=True)
            sleep(0.5)
        print()
        with open("notas.json", 'r+') as f:
            notas = json.load(f)
        print('Arquivo carregado com sucesso!')
    elif r == 4: #salvar lista
        print('Salvando',end='')
        for c in range (0,3):
            print('.',end='',flush=True)
            sleep(0.5)
        print()
        with open("notas.json", 'r+') as f:
            json.dump(notas, f, indent=2) 
        print('Arquivo salvo com sucesso!')
    elif r == 5:
        print('Tenha um bom dia!')
        break
    else:
        print('Opção inválida! Tente novamente.')
linhas()
