while True:
    try:
        nota = float(input('Digite uma nota entre 0 a 10 ? '))

        if 0 <= nota <= 10:
            print(f'A nota {nota} foi a que você escolheu. Nota válida!')
            break
        else:
            print('Nota inválida!')

    except ValueError:
        print('Isso não é um número!')

#Peça para o usuário digitar uma nota de 0 a 10 (pode ser decimal, tipo 7.5).
#Tente converter essa entrada para um número de ponto flutuante (float).
#Se o valor não for um número válido, avisa o usuário e continua  o programa.
#Se o número for válido, mas fora da faixa de 0 a 10, avisa que a nota é inválida e continua.
#Se estiver tudo certo, imprime a nota com a mensagem:
#"A nota {} foi a que você escolheu. Nota válida!

