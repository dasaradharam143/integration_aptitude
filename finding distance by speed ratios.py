condition = input("1)To find race distance or 2)To find win by = ")

if condition == "1":
    A_speed_ratio = int(input("speed ratio of A ="))
    B_speed_ratio = int(input("speed ratio of B ="))
    speed_gain_by_winner = (A_speed_ratio-B_speed_ratio)
    A_gives_start_to_B = float(input("A gives a start ="))
    race_distance = (A_speed_ratio*A_gives_start_to_B/speed_gain_by_winner)
    print(f"race distance = {A_speed_ratio}*{A_gives_start_to_B}/{speed_gain_by_winner}")
    print("race distance=" + str(race_distance) + "m")

else:
    race_distance = float(input("race distance ="))
    A_speed_ratio = int(input("speed ratio of A ="))
    B_speed_ratio = int(input("speed ratio of B ="))
    A_is_start_of_B = float(input("A has start of B ="))

    distance_covered_A = (race_distance - A_is_start_of_B)
    print(f'distance covered by A = {race_distance}-{A_is_start_of_B}')
    print("distance covered by A =" + str(distance_covered_A))

    distance_covered_B = (B_speed_ratio/A_speed_ratio*distance_covered_A)
    print(f'distance covered by B = {B_speed_ratio}/{A_speed_ratio}*{distance_covered_A}')
    print("distance covered by B =" + str(distance_covered_B))

    A_wins_by = (race_distance - distance_covered_B)
    print(f'A wins by = {race_distance}-{distance_covered_B}')
    print("A wins by =" + str(A_wins_by) + "m")
