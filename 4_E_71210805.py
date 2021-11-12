print("4_E_71210805")
a = float(input("\na : "))
U2 = float(input("U2 : "))
r = U2/a
A1 = (a*((r**11)-1))/r-1
A2 = (a*(1-r**11))/1-r
if (r > 1):
    print("\nS11 = %0.2f" %A1)
else:
    print("S11 = %0.2f" %A2)
