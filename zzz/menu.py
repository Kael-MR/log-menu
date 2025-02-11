from ferramentas import ferr

ferr.linhas('MENU LOGINS:')
ferr.linhas('''
1-see logins
2-add new login
3-out of code''')

while True:
    decmenu = int(input('choice?'))

    if decmenu < 1:
        print('invalid option, try again')
    elif decmenu > 3:
        print('invalid option, try again') 

    elif decmenu == 3:
        ferr.linhas('END OF CODE, ja ane')
        break

    else:
        ferr.demenu(decmenu)

print('REAL END CODE')
