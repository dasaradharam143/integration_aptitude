condition = input("1)win percentage or 2)lost percentage = ")
if condition == "1":
    total_matches_played = int(input("total matches played = "))
    matches_win = int(input("matches win = "))
    winning_percentage = (matches_win/total_matches_played*100)

    print(f"winning percentage = {matches_win}/{total_matches_played}*{100}")
    print("winning percentage =" + str(winning_percentage) + "%")

else:
    total_matches_played = int(input("total matches played = "))
    matches_win = int(input("matches win = "))
    matches_lost = total_matches_played - matches_win
    matches_lost_percentage = (matches_lost/total_matches_played*100)

    print(f"lost percentage = {matches_lost}/{total_matches_played}*{100}")
    print("lost percentage =" + str(matches_lost_percentage) + "%")
