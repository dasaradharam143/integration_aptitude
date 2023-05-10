from subprocess import call

def option():
    condition = input('1)2_contestants different distance 2)2_and_3_contestants for finding time '
                  '\n3)2_contestants to find distance by time 4)3_contestants same distance '
                  '\n5)3_contestants with 2 distances 6)3_different distances  7)finding distance by speed ratios'
                  '\n 8)finding 2 speeds 9) to find one speed  10) members game'
                  '\n11)to find loss or win percent   PRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = 'two_contestants_with_different_distance.py'
    elif condition == '2':
        value = 'two_contestants_for_finding_time.py'
    elif condition == '3':
        value = 'two_contestants_to_find_distance_by_time.py'
    elif condition == '4':
        value = 'three_contestants_same_distance.py'
    elif condition == '5':
        value = 'three_contestants_with_two_distances.py'
    elif condition == '6':
        value = 'three_contestants_with_three_different_distances.py'
    elif condition == '7':
        value = 'finding_distance_by_speed_ratios.py'
    elif condition == '8':
        value = 'finding_two_speeds.py'
    elif condition == '9':
        value = 'to_find_speed.py'
    elif condition == '10':
        value = 'members_game.py'
    elif condition == '11':
        value = 'to_find_loss_or_win_percent.py'

    else:
        exit()
    return value


def openpyfile():
    call(['python',option()])
    print()
    print('/////////////////////////////////////////////////////////')
    openpyfile()

openpyfile()
