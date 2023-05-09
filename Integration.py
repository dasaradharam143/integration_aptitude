from subprocess import call

def option():
    condition = input('1)2_contestants different distance 2)2_and_3_contestants for finding time '
                  '\n3)2_contestants to find distance by time 4)3_contestants same distance '
                  '\n5)3_contestants with 2 distances 6)3_different distances  7)finding distance by speed ratios'
                  '\n 8)finding 2 speeds 9) to find one speed  10) members game'
                  '\n11)to find loss or win percent   PRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = '2 contestants diff distance.py'
    elif condition == '2':
        value = '2 contestants for finding time.py'
    elif condition == '3':
        value = '2 contestants to find distance by time.py'
    elif condition == '4':
        value = '3 contestants same distance.py'
    elif condition == '5':
        value = '3 contestants with 2 distances.py'
    elif condition == '6':
        value = '3 different distances.py'
    elif condition == '7':
        value = 'finding distance by speed ratios.py'
    elif condition == '8':
        value = 'finding 2 speeds.py'
    elif condition == '9':
        value = 'to find speed.py'
    elif condition == '10':
        value = 'four members game.py'
    elif condition == '11':
        value = 'to find loss or win percent.py'

    else:
        exit()
    return value


def openpyfile():
    call(['python',option()])
    print()
    print('/////////////////////////////////////////////////////////')
    openpyfile()

openpyfile()
