from subprocess import call


def option():
    condition = input('1)Average 2)Races and games'
                      '\n3)stocks and shares'
                      '\nPRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = 'run.py'
    elif condition == '2':
        value = 'Integration.py'
    elif condition == '3':
        value = 'call_function.py'

    else:
        exit()
    return value


def openpyfile():
    call(['python', option()])
    print(' ')
    print('/////////////////////////////////////////////////////////')
    print(' ')
    openpyfile()


openpyfile()
