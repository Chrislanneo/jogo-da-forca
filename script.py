import random
import os

def linha():
    linha = '-' * 80
    print(linha)

def cabecalho():
    titulo = 'JOGO DA FORCA'
    linha()
    print(titulo.center(80))
    linha()


def instrucoes():
    print(
        'INSTRUÇÕES: O jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras e o tema '
        'ligado à palavra. A cada letra errada, é desenhado uma parte do corpo do enforcado. O jogo termina ou com o '
        'acerto da palavra ou com o término do preenchimento das partes corpóreas do enforcado.\n')


def menu_iniciar():
    cabecalho()
    modo_iniciar = int(input('Olá você deseja ler as intruções?\n [1] Sim\n [2] Não\n'))
    if modo_iniciar == 1:
        instrucoes()
        input('Pressione ENTER para continuar')
    elif modo_iniciar == 2:
        input('Pressione ENTER para continuar')
    else:
        print('Desculpe, não entendi.')
        menu_iniciar()

    os.system('cls' if os.name == 'nt' else 'clear')
def escolhe_tema():
    cabecalho()
    global arquivo
    tema = int(input("Escolha um tema para a palavra secreta\n TEMAS:\n [1] Cores\n [2] Frutas\n"))

    if tema == 1:
        arquivo = open("cores.txt")
    elif tema == 2:
        arquivo = open("frutas.txt")
    else:
        print('Digite uma opção válida.')
        escolhe_tema()

    palavras: list[str] = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    return palavras


def define_palavra():
    palavras = escolhe_tema()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def pede_chute():
    chute = input("Chute letra: ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, acertos, palavra_secreta):
    index = 0
    if chute == palavra_secreta:
        for letra in chute:
            acertos[index] = letra
            index += 1

    for letra in palavra_secreta:
        if (chute == letra):
            acertos[index] = letra
        index += 1


def forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vitoria():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_derrota(palavra_secreta):
    print('Você foi enforcado!')
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():
    menu_iniciar()
    palavra_secreta = define_palavra()

    acertos = ['_' for letra in palavra_secreta]
    print(f'\nA palavra secreta possui {len(palavra_secreta)} letras. Boa sorte!\n')
    print(acertos)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, acertos, palavra_secreta)
        else:
            erros += 1
            forca(erros)

        enforcou = erros == 7
        acertou = '_' not in acertos

        print(acertos)

    if (acertou):
        mensagem_vitoria()
    else:
        mensagem_derrota(palavra_secreta)

    input('')



if __name__ == "__main__":
    jogar()
