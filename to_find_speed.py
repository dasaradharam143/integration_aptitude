condition = input("need to find speed = 1)kph or 2)m/sec =")
if condition == "1":
    A_distance = float(input("A covered distance ="))
    A_gives_B = float(input("A gives B a Start of ="))
    B_distance = A_distance-A_gives_B
    print(f'B distance covered = {A_distance}- {A_gives_B}')
    print(f'B distance covered= {B_distance}')

    A_speed = float(input("speed of A = "))*(5/18)
    A_beat_B = float(input("A beats by B in secs ="))
    time_taken_by_A = (A_distance/A_speed)
    print(f'time taken by A = {A_distance}/{A_speed}')
    print("time taken by A =" + str(time_taken_by_A)+"sec")

    time_taken_by_B = time_taken_by_A + A_beat_B
    print(f'time taken by B = {time_taken_by_A} +{A_beat_B}')
    print("time taken by B =" + str(time_taken_by_B)+"sec")

    B_speed = (B_distance/time_taken_by_B)*(18/5)
    print(f'speed B = {B_distance}/{time_taken_by_B}*{18/5}')
    print("Speed of B =" + str(B_speed) + "kph")
else:
    A_distance = float(input("A distance ="))
    A_gives_B = float(input("A gives B a Start of ="))
    B_distance = A_distance-A_gives_B
    print(f'B distance covered = {A_distance}- {A_gives_B}')
    print(f'B distance covered= {B_distance}')

    A_speed = float(input("speed of A = "))*(18/5)
    A_beat_B = float(input("A beats by B in secs ="))
    time_taken_by_A = (A_distance/A_speed)
    print(f'time taken by A = {A_distance}/{A_speed}')
    print("time taken by A =" + str(round(time_taken_by_A, 5))+"sec")

    time_taken_by_B = time_taken_by_A + A_beat_B
    print(f'time taken by B = {time_taken_by_A} +{A_beat_B}')
    print("time taken by B =" + str(round(time_taken_by_B, 5))+"sec")

    B_speed = (B_distance/time_taken_by_B)
    print(f'speed B = {B_distance}/{time_taken_by_B}')
    print("Speed of B =" + str(round(B_speed, 5)) + "m/sec")
