def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt)
    print(linha())



def menu(lista):
    cabeçalho('menu principal')
    c=1
    for item in lista:
        print(f'{c}-{item}')
        c+=1
    print(linha)
    opc=leiaint('sua opção')
    return opc



def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('erro digite um numero inteiro  valido ')
            continue
        except (KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n




