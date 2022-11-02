from verificaçãoERRO.lib.interface import cabeçalho
def arquivoexiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('houve um errro em ecrever os dados')
        else:
            print(f'novo registro{nome}adicionado')





def criararquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('houve um erro ')
    else:
        print(f'arquivo {nome} ')


def lerarquivo(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Errro ao ler')
    else:
        cabeçalho('pessoas cadastradas ')
        print(a.read())
