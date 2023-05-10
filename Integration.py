from subprocess import call


def option():
    condition = input('1)two_contestants_different_distance 2)two_and_three_contestants_for_finding_time '
                      '\n3)two_contestants_to_find_distance_by_time 4)three_contestants_same_distance '
                      '\n5)three_contestants_with_two_distances 6)three_different_distances '
                      '\n7)finding_distance_speed ratios 8)finding_two_speeds 9) to_find_one_speed'
                      '\n 10) members_game 11)to_find_loss_or_win_percent'
                      '\n PRESS_0_TO_EXIT_enter_option = ')

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
    call(['python', option()])
    print()
    print('/////////////////////////////////////////////////////////')
    openpyfile()


openpyfile()
