
from subprocess import call

def option():
    condition = input('Stocks&Shares PRESS 0 TO EXIT enter option : ')
    value = ''
    if condition == '1':
        value = 'stocks_shares.py'
    else:
        exit()
    return value

def openpyfile():
    call(['python', option()])
    print()
    print('/////////////////////////////////////////////////////////')
    openpyfile()

openpyfile()
