condition = input("1)two contestants or 2)three contestants =")

if condition == "1":
    race_distance = float(input("Enter the race distance in meters="))
    A_beat_B_distance = float(input("Enter A beats by B distance in meters="))
    A_beat_B_time = float(input("Enter A beats by B time in sec="))
    time_taken_B = (A_beat_B_time/A_beat_B_distance*race_distance)

    print(f'time taken by B = {A_beat_B_time}/{A_beat_B_distance}*{race_distance}')
    print("Time taken by B ="+str(time_taken_B)+"sec")

    time_taken_A = (time_taken_B - A_beat_B_time)
    print(f'time taken by A = {time_taken_B}-{A_beat_B_time}')
    print("Time taken by A ="+str(time_taken_A)+"sec")

else:
    race_distance = float(input("Enter the race distance in meters="))
    A_beat_B_time = float(input("Enter A beats by B time in sec="))
    B_beat_C_time = float(input("Enter A beats by C time in sec="))
    A_beat_C = float(input("Enter A beats C distance ="))
    time_taken_C = (A_beat_B_time + B_beat_C_time)
    print(f' time taken by C = {A_beat_B_time} +{B_beat_C_time} sec')
    print("Time taken by C ="+str(time_taken_C)+"sec")

    total_time_taken_C = (time_taken_C/A_beat_C*race_distance)
    print(f'total time taken by C ={time_taken_C}/{time_taken_C}*{race_distance}')

    time_taken_A = (total_time_taken_C-time_taken_C)
    print(f'Time taken by A = {total_time_taken_C}-{time_taken_C}')
    print("Time taken by A ="+str(time_taken_A)+"sec")
