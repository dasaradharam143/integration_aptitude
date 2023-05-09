
A_beat_B = float(input("A beat B="))
B_beat_C = float(input("B beat C="))
A = float(input("Winner distance of A= "))
B = A - A_beat_B
print(f'B distance covered = {A}-{A_beat_B}')
print(f'B distance covered = {B}')
b = float(input("Winning distance of b="))
C = b - B_beat_C
print(f'C distance covered = {b}-{B_beat_C}')
print(f'B distance covered = {C}')
distance = (A / B * b / C)
print(f'distance = {A}/{B}*{b}/{C}')
print(f'distance = {round(distance, 3)}')
a_beat_c = float(input("A beat C in how much distance="))
A_beat_C = a_beat_c - (a_beat_c / distance)
print("A_beat_C =" + str(A_beat_C) + "m")
