#Cifra de César em Phyton
import sys
import os
Tamanho = 26
print('Pressione ENTER para começar')
def reiniciar():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def Modo():
    while True:
        modo = input().lower()
        if modo in 'e d'.split():
            return modo
        else:
            print('Digite "e" para encriptar ou "d" para desencriptar')
def Mensagem():
    print('Digite a mensagem: ')
    return input()
def Chave():
    chave = 0
    while True:
        print('Digite uma chave numerica (1-%s)' % (Tamanho))
        chave = int(input())
        if (chave >= 1 and chave <= Tamanho):
            return chave
def Mensagem_Traduzida(modo, mensagem, chave):
    if modo[0] == 'd':
        chave = -chave
    traducao = ''
    for letra in mensagem:
        if letra.isalpha():
            num = ord(letra)
            num += chave
            if letra.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letra.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traducao += chr(num)
        else:
            traducao += letra
    return traducao

modo = Modo()
Loop = True
while (Loop):
    mensagem = Mensagem()
    total = 0
    for letras in mensagem:
        total = total + 1
    if total > 128:
        print("------------------------------------")
        print("Limite de 128 caracteres excedido")
        print("------------------------------------")
        reniciar= reiniciar()
    else:
        Loop = False
chave = Chave()
print('\nSeu texto é: ', end='')
print(Mensagem_Traduzida(modo, mensagem, chave))
print("------------------------------------")
print("fim")
reniciar= reiniciar()