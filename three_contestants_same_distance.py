def A_beat_C():
    A_beat_B=int(input("A beat B="))
    B_beat_C=int(input("B beat C="))
    A=int(input("Winner distance of A= "))
    B=A-A_beat_B
    print(f'B covered distance = {A} - {A_beat_B} ')
    b=int(input("Winning distance of b="))
    C=b-B_beat_C
    print(f'A covered distance ={b}-{B_beat_C}')
    distance=(A/B*b/C)
    print(f'distance ={A}/{B}*{b}/{C}')
    A_beat_C=A-(A/distance)
    print(f'A beat C= {A}-{A}/{distance}')
    return  A_beat_C

def B_beat_C():
    B_beat_A=int(input("B beat A="))
    A_beat_C=int(input("A beat C="))
    B=int(input("Winner distance of B= "))
    A=B-B_beat_A
    print(f'A = {B} - {B_beat_A} ')
    a=int(input("Winning distance of a="))
    C=a-A_beat_C
    print(f'A ={a}-{A_beat_C}')
    distance=(B/A*a/C)
    print(f'distance ={B}/{A}*{a}/{C}')
    B_beat_C=B-(B/distance)
    print(f'B beat C= {B}-{B}/{distance}')
    return B_beat_C

def C_beat_A():
    C_beat_B=int(input("C beat B="))
    B_beat_A=int(input("B beat A="))
    C=int(input("Winner distance of C= "))
    B=C-C_beat_B
    print(f'B = {C} - {C_beat_B} ')
    b=int(input("Winning distance of b="))
    A=b-B_beat_A
    print(f'A ={b}-{B_beat_A}')
    distance=(C/B*b/A)
    print(f'distance ={C}/{B}*{b}/{A}')
    C_beat_A=C-(C/distance)
    print(f'C beat A= {C}-{C}/{distance}')
    return C_beat_A

condition=input("1)A_beat_C or 2)B_beat_C or 3)C_beat_A=")
if condition=="1":
    print("A_beat_C="+str(A_beat_C()) + 'm')

elif condition=="2":
    print("B_beat_C="+str(B_beat_C()) + 'm')

else:
    print("C_beat_A="+str(C_beat_A()) + 'm')

