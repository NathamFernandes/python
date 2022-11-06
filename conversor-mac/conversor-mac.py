while True:

    ## Declarando variáveis
    
    endereco_entrada = str(input("Insira o endereço MAC: "))
    tipo =  int(input('- Windows "-" (1) \n- Intelbras "." (2) \n- HP ":" (3) \n \nInsira para qual tipo você quer converter: '))
    elementos = list(endereco_entrada)
    quantidade = len(elementos)
    nova_lista = []
    endereco_saida = []
    num = 0

    ## Condição de endereço MAC
    ## 17 = Endereço MAC com separação - (apenas conversão do separador para o tipo desejado)
    ## 12 = Endereço MAC sem separação - (adição do separador para o tipo desejado)
    
    if quantidade == 17:
        if tipo == 1:
            elementos[2] = "-"
            elementos[5] = "-"
            elementos[8] = "-"
            elementos[11] = "-"
            elementos[14] = "-"
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (Windows): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
        elif tipo == 2:
            elementos[2] = "."
            elementos[5] = "."
            elementos[8] = "."
            elementos[11] = "."
            elementos[14] = "."
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (Intelbras): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
        elif tipo == 3:
            elementos[2] = ":"
            elementos[5] = ":"
            elementos[8] = ":"
            elementos[11] = ":"
            elementos[14] = ":"
            endereco_saida = ''.join(elementos)
            print("Enderço MAC (HP): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
        else:
            print("Opção inválida. Programa encerrado.")
    elif quantidade == 12:
        for x in elementos:
            nova_lista.append(x)
            num = num + 1
            if num % 2 == 0:
                if tipo == 1:
                    nova_lista.append("-")
                elif tipo == 2:
                    nova_lista.append(".")
                elif tipo == 3:
                    nova_lista.append(":")
        nova_lista.pop()
        endereco_saida = ''.join(nova_lista)
        if tipo == 1:
            print("Enderço MAC (Windows): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
        elif tipo == 2:
            print("Enderço MAC (Intelbras): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
        elif tipo == 3:
            print("Enderço MAC (HP): " + endereco_saida)
            continuar = str(input("Deseja encerrar o programa? [S/N]: "))
            if continuar.upper() == "S":
                break
    else:
        print("\nSeparação inválida. Insira uma separação válida ('-', ':', '-', '')\n")
