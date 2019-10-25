# Esse projeto simula um jogo de roleta

def roleta():

    jogar = 'S'

    while jogar == 'S':

        aposta = int(input('Faça sua aposta! Escolha um número entre 0 e 36: '))
        cor_aposta = ''
        cor_sorteada = ''

        vermelho = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] #números vermelhos na roleta

        print(' vamos rodar a roleta...')

        import random #biblioteca que permite retornar um número aleatório

        def aleat():
            for x in range(1):
                lista = random.randrange(0,36,1)# função que faz o sorteio

            print('E o número da roleta foi...')

            print('foi o número {} '.format(lista))

            return lista

        result = aleat()
        #print (result)

        #verifica se o número apostado foi vermelho ou preto
        if aposta in vermelho:
            cor_apostada = 'Vermelho'
        else:
            cor_apostada = 'Preto'

        #verifica se o resultado da roleta é um número vermelho ou preto
        if result in vermelho:
            cor_sorteada = 'Vermelho'
        else:
            cor_sorteada = 'Preto'

        #verifica se o número apostado é par ou impar
        def parimpar():
            if aposta%2 ==0:
                return "par"
            else:
                return "impar"

        apostapar = parimpar()

        #verifica se o número sorteado é par ou impar
        def parimparsorteio():
            if result%2 ==0:
                return "par"
            else:
                return "impar"

        sorteiopar = parimparsorteio()

        #informa a cor sorteada
        print ("A cor do número sorteado é:", cor_sorteada)
        print ("A cor do número informado é:", cor_apostada)
        print (" ")

        #Verifica o resultado do sorteio
        if aposta == result:
            print ("Parabéns, você ganhou o prêmio máximo")
        elif cor_apostada == cor_sorteada and apostapar == sorteiopar:
            print ("Você acertou a cor e se o número é par ou impar -- Segundo Prêmio")
        elif cor_apostada == cor_sorteada:
            print ("Você acertou a cor - Terceiro Prêmio ")
        elif apostapar == sorteiopar:
            print ("Você acertou se o número é par ou impar -- Ultimo prêmio")
        else:
            print("Você perdeu!!!")
        print (" ")
        jogar = input("Deseja jogar de novo? S/N ")

roleta() 
    


    
