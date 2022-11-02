from verificaçãoERRO.lib.interface import *
from verificaçãoERRO.lib.arquivo import *

arq='cursola.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta=menu(['ver pessoas cadastradas','cadastrar nova pessoa','sair do sis'])
    if resposta==1:
        lerarquivo(arq)
    elif resposta ==2:
        cabeçalho('novo cadastratro')
        nome=str(input('nome'))
        idade=leiaint('idade')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        print('ate mais')
        break
    else:
        print('erro ')