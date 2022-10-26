def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not acertou and not enforcou:

        chute = input('Digite a palavra: ').strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
                print(f'Encontrei a letra {chute} na posição {index}')
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
