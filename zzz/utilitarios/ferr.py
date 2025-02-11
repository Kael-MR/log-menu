import os
logins = list()


def linhas(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(msg)
    print('~'*tam)


def demenu(n):

    if n == 1:
        os.system('cls')
        linhas('THOSE ARE THE LOGINS')
        for c in range(0, len(logins)):
            print(logins[c])
    
    
    elif n == 2:
        linhas('CREATING AN NEW LOGIN')
        for c in range(0, 999):

            ll = dict() 
            nick = input('login: ')
            pas = input('password: ')
            ll['nick'] = nick
            ll['password'] = pas
            logins.append(ll)
            ll.clear

            dec2 = str(input('more login?[S/N]'))
            if dec2 in 'Nn':
                print('ok, ja ane')
                break
            elif dec2 in 'Ss':
                print('')
            else:
                print('option invalid, try again')
