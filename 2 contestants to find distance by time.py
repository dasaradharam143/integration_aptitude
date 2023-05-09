
race_distance = int(input("enter race distance = "))
time_taken_by_winner = int(input("enter time taken by winner = "))
time_taken_by_losser = int(input("enter time taken by losser = "))
time_difference = time_taken_by_losser - time_taken_by_winner
winner_beats_by_losser = (race_distance / time_taken_by_losser * time_difference)
print(f' winner beat losser = {race_distance}/{time_taken_by_losser}*{time_difference}')
print("winner_beat_losser =" + str(winner_beats_by_losser) + 'm')
