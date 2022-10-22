#display nickname using asterisk
#codes for letters R,A,H 
for row in range (7):
    for col in range (17):
        if ((col==0) or ((row==0 or row==3) and (col>0 and col<4)) or ((col==4) and (row!=0 and row!=3))):
        
            print("*", end=" ")
            
        else:
            print(end="  ")

    print()