v1 = int(input('valor 1 '))
v2 = int(input('valor 2'))
v3 = int(input('valor3'))
menor = v1
if v2<v1 and v2<v3:
    v2 = menor
if v3 <v1 and v3<v2:
    menor = v3
maior = v1
if v2 >v1 and v2>v3:
    maior = v2
if v3 > v1 and v3 >v2:
    maior= v3
print('o maior valor é {}'.format(maior))
print('o menor valor é {}'.format(menor))
