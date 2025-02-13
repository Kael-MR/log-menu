import os
logins = list()
logins2 = list()

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
            logins2.append(nick)
            logins2.append(pas)
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


def create_file():
    vetor = 0
    
    arquivo = open('real/login_register.txt', 'a')
    arquivo.write('LOGINS AND PASS\n')
    arquivo.close()
    for c in range(0, len(logins2)):
            
            if vetor %2 == 0:
                string = ''.join(logins2[vetor])
                arquivo = open('real/login_register.txt', 'a')
                arquivo.write(f'\nlogin: {string}')
            else:
                string = ''.join(logins2[vetor])
                arquivo = open('real/login_register.txt', 'a')
                arquivo.write(f'\npassword: {string}')

            arquivo.close()
            vetor += 1
             
