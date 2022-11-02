def aumentar(preço=0,taxa=0,formato=False):
    res= preço + (preço*taxa/100)
    return res if  formato is False  else moeda(res)



def diminuir(preço=0,taxa=0,formato=False):
    res= preço-(preço*taxa/100)
    return res if  formato is False else  moeda(res)



def metade(preço=0,formato=False):
    res=preço/2
    return res if formato is False  else moeda(res)



def dobro(preço=0,formato=False):
    res=preço *2
    return res if  formato is False else moeda(res)



def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço}'.replace('.',',')



def resumo(preço=0,taxaa=10,taxar=5):
    print(f'preço analisado:{preço}')
    print(f'o dobro do preço é {dobro(preço,True)}')
    print(f'a metade do preço é{metade(preço,True)}')
    print(f' com aumento:{aumentar(preço,taxaa,True)}')
    print(f'com desconto{diminuir(preço,taxar,True)}')


