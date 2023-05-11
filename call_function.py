from subprocess import call


def option():
    condition = input('1)stocks_shares PRESS 0 TO EXIT enter option : ')
    ''
    if condition == '1':
        value = 'stocks_shares.py'
    elif condition == '0':
        exit()
    return value


def openpyfile():
    call(['python', option()])
    print()
    print('--------------------------------------------------------')
    openpyfile()


openpyfile()
