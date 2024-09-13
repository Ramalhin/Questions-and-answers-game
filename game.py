import os

perguntas = [
    {'pergunta': 'quanto é:   1+1',
     'opções': ['1', '2', '3'],
     'correta': '2'},
    {'pergunta': 'quanto é:   2+2',
     'opções': ['4', '5', '6'],
     'correta': '4'},
    {'pergunta': 'quanto é:   1-1',
     'opções': ['0', '1', '2'],
     'correta': '0'}
]


def iniciarJogo():
    pontuacao = 0
    print('vamos jogar um jogo de perguntas e respostas')

    for pergunta in perguntas:
        while True:
            print('pergunta:', pergunta['pergunta'])
            print()
            opcoes = pergunta['opções']
            for i, opcao in enumerate(opcoes):
                print(f'{i}) {opcao}')
            print()
            resposta = input('qual a resposta? ')
            correta = pergunta['correta']

            if resposta.isdigit():
                escolhaInt = int(resposta)
                if 0 <= escolhaInt < len(opcoes):
                    if opcoes[escolhaInt] == correta:
                        pontuacao += 1
                        print('acertou')
                        break
                    else:
                        print('errou')
                        break
                else:
                    print('opção inválida')
            else:
                print('Por favor, digite um número.')

            print()

    return pontuacao


pontuacao_final = iniciarJogo()

os.system('cls')
print(f'Você acertou um total de\n {pontuacao_final}/{len(perguntas)} perguntas')