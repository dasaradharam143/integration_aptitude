
a_beat_b = int(input("A beat B="))
b_beat_c = int(input("B beat C="))
a = int(input("Winner distance of A= "))
b = a - a_beat_b
print(f'B covered distance = {a} - {a_beat_b} ')
print(f'B covered distance = {b}')
B = int(input("Winning distance of b="))
c = B - b_beat_c
print(f'A covered distance ={B}-{b_beat_c}')
print(f'C covered distance = {c}')
distance = (a / b * B / c)
print(f'distance ={a}/{b}*{B}/{c}')
a_beat_c = a - (a / distance)
print(f'A beat C= {a}-{a}/{distance}')
print("A_beat_C=" + str(a_beat_c()) + 'm')
