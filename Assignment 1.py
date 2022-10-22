#display nickname using asterisk

for row in range (7):
    for col in range (17):
       if ((col==0) or ((row==0 or row==3) and (col>0 and col<4)) or ((col==4) and (row!=0 and row!=3)) or
            ((row==0 or row==3) and (col>6 and col<10)) or ((col==6 or col==10) and (row!=0))or
            ((col== 12 or col==15)) or (row==3 and (col>12 and col<15))):
        
            print("*", end=" ")
            
        else:
            print(end="  ")

    print()