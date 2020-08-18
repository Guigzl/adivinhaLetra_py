secreto = input("Escreva umna letra")
digitadas = []
chances = 4

while True:
    if chances == 0:
        print('você perdeu')
        break

    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print('digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabéns você adivinhou uma letra: {letra}')
    else:
        print(f'Infelizmente a letra {letra} não confere')
        digitadas.pop()


    secreto_temp = ''
    for letra_sec in secreto:
        if letra_sec in digitadas:
            secreto_temp += letra_sec
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f"PARABEEEENS VOCÊ ACERTOU A PALAVRA {secreto.title()}")
        break
    else:
        print(f'até agora a palavra está {secreto_temp}')

    if letra not in secreto:
        chances -= 1

    print(f'você ainda tem {chances} chances')
    print()

