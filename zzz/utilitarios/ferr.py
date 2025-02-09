def linhas(msg):
    tam = len(msg) + 4
    print('-'* tam)
    print(msg)
    print('-'*tam)



def dec(n):
    while True:
        if n == 1:
            linhas('OPTION 1')
            break
        elif n == 2:
            linhas('OPTION 2')
            break
        
        else:
            print('ERROR, try again')
    

galera = list()
def rmenu(opc):
    if opc == 1:
        linhas('those are the logged persons: ')
        linhas(galera)
    elif opc == 2:
        pessoa = str(input('whats the name? '))
        galera.append(pessoa)

