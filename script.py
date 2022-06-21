import getpass
import os

def cabecalho():
    
    linha = '-' * 80
    titulo = 'JOGO DA FORCA'
    print(linha)
    print(titulo.center(80))
    print(linha)
def instrucoes():
    print('INSTRUÇÕES: O jogo da forca consiste na adivinhação de uma palavra secreta deteminada por um dos participantes. Os demais irão chutar letras completando a palavra antes que as chances acabem.\n')
def jogar():
    os.system('cls') or None
    cabecalho()

    palavra_secreta = getpass.getpass('Vamos começar...\nQual a palavra secreta? \n')
    palavra_secreta = palavra_secreta.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    chances = 6
    
    print(f'A palavra secreta possui {len(palavra_secreta)} letras. Você possui {chances} chances. Boa sorte!')
    print(letras_acertadas)

    acertou = False
    enforcou = False

    while not enforcou and not acertou:
        chute = input('Digite uma letra...')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index +=1    
        else:
            chances -= 1
    
        enforcou = chances == 0
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!')
    
    print('Fim de Jogo')
def inicio():
    modo_iniciar = int(input('Olá você deseja ler as intruções?\n [1] Sim\n [2] Não\n'))
    if modo_iniciar == 1:
        instrucoes()
        input('Pressione ENTER para continuar')
        jogar()
    elif modo_iniciar == 2:
        jogar()
    else:
        print('Desculpe, não entendi.')
        inicio()

cabecalho()
inicio()