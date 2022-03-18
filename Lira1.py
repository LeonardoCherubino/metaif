#Python Impressionador - Aula de IF
meta = int(input('Entre com o valor da meta: '))
quantidade_vendida = int(input('Entre com a quantidade de vendas: '))

if quantidade_vendida > meta:
    print('A quantidade vendida foi de {}, batemos a meta.'.format(quantidade_vendida))
else:
    print('Infelizmente não batemos a meta')