A = float(input("A runs a distance ="))
B = float(input("B runs a distance ="))
distance = (B/A)
print(f'distance = {B/A}')

dif_distance = float(input("B beat A in how much distance ="))
B_beat_A = dif_distance-(dif_distance/distance)
print(f'B beat A = {dif_distance}- {dif_distance}/{distance}')
print("B beats by A =" + str(B_beat_A) + "m")
