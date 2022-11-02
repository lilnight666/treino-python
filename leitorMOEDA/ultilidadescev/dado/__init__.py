def leiadinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == ' ':
            print(f'{entrada} é invalido ')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('erro digite um numero inteiro')
        if ok:
            break

    return valor


