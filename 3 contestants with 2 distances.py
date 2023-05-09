
condition = input("1)B_beat_C or 2)C_beat_B=")

if condition == "1":
    A_beat_B = float(input("A beat B="))
    A_beat_C = float(input("A beat C="))
    A = float(input("Winner distance of A= "))
    B = A - A_beat_B
    print(f'B distance covered = {A}-{A_beat_B}')
    print(f'B distance covered = {B}')
    C = A - A_beat_C
    print(f'C distance covered = {A}-{A_beat_C}')
    print(f'B distance covered = {C}')
    distance = (B/A * A/C)
    print(f'distance = {B}/{A}*{A}/{C}')
    print(f'distance = {round(distance ,3)}')
    b_beat_c = float(input("B beat C in how much distance="))
    B_beat_C = b_beat_c - (b_beat_c / distance)
    print(f'B beat C = {b_beat_c}-{b_beat_c}/{distance}')
    print("B_beat_C =" + str(B_beat_C) + "m")
else:
    A_beat_B = float(input("A beat B="))
    A_beat_C = float(input("A beat C="))
    A = float(input("Winner distance of A= "))
    B = A - A_beat_B
    print(f'B distance covered = {A}-{A_beat_B}')
    print(f'B distance covered = {B}')
    C = A - A_beat_C
    print(f'C distance covered = {A}-{A_beat_C}')
    print(f'B distance covered = {C}')
    distance = (C/A * A/B)
    c_beat_b = float(input("C beat B in how much distance="))
    C_beat_B = c_beat_b - (c_beat_b / distance)
    print(f'B beat C = {c_beat_b}-{c_beat_b}/{distance}')
    print("C_beat_B =" + str(C_beat_B) + 'm')
