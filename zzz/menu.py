from utilitarios import ferr
galerap = ferr.galera[:]

ferr.linhas('MENU PRINCIPAL')
ferr.linhas('''
1-see logged people
2-new login 
3-exit''')

while True:
    dmenu = int(input('choice? '))
    if dmenu > 3:
        print('option not understood, try again')
    elif dmenu < 1:
        print('option not understood, try again')
    elif dmenu == 3:
        ferr.linhas('END OF CODE, ja ane')
        break

    else:
        ferr.rmenu(dmenu)

print('REAL END CODE')