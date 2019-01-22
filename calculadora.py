# CALCULADORA

# -----
# funções
soma = lambda x,y:x+y
sub = lambda x,y:x-y
mult = lambda x,y:x*y
div = lambda x,y:x/y

def imprime(r):
    print('O resultado é %.3f\n\n' %(r))
    
def opera(op, x, y):
    if op == 1:
        r = soma(x,y)
    if op == 2:
        r = sub(x,y)
    if op == 3:
        r = mult(x,y)
    if op == 4:
        r = div(x,y)    
    return r

# -----
print('-----CALCULADORA PYTHON-----\n')

rep = 1
while rep == 1 or rep == 2:
    op = int(input('POR FAVOR, ESCOLHA A OPERAÇÃO DESEJADA:\n1) ADIÇÃO\n2) SUBTRAÇÃO\n3) MULTIPLICAÇÃO\n4) DIVISÃO\n'))
    
    while(op != 1 and op != 2 and op != 3 and op != 4):
        op = int(input('Opção não existente. Por favor, digite novamente:'))

    if rep == 1:
        x = float(input('Digite o primeiro número:'))
        y = float(input('Digite o segundo número:'))
        while y == 0 and op == 4:
            print('Indeterminacao!\nPor favor, nao use zero no numerador!\n')
            y = float(input('Digite o segundo número:'))
        r = opera(op, x, y)
        imprime(r)
        
    if rep == 2: # para fazer a operação com o resultado obtido anteriormente
        print('O resultado obtido anteriormente foi %.3f' %(r))
        y = float(input('Digite o segundo número:'))
        while y == 0 and op == 4:
            print('Indeterminacao!\nPor favor, nao use zero no numerador!\n')
            y = float(input('Digite o segundo número:'))
        r = opera(op, r, y)
        imprime(r)
    
    rep = int(input('Se desejar fazer outra operação, digite 1.\nSe desejar fazer outra operação com o resultado obtido, digite 2.\nSe deseja encerrar, digite qualquer outro número:\n'))
