import random

dice=[1,2,3,4,5,6]
total_no=[0,0,0,0,0,0]
longest_row=[0,0,0,0,0,0]
final_role=0

def role():
    dice=random.randint(1,6)
    print(dice)
    return dice

def One_M_rols():
    count=0
    temp_lr = [0, 0, 0, 0, 0, 0]
    while count<=1000000:
        count+=1
        roled=role()
        total_no[roled-1]+=1
        temp_lr[roled-1]+=1
        for num in dice:
            if longest_row[num-1]<temp_lr[num-1] and num != roled:
                longest_row[num-1]=temp_lr[num-1]
                temp_lr[num - 1]=0
        final_role =roled

def display():
    print("the dice is on fier\n")
    for num in dice:
        print("total no of "+str(num)+" apperd = "+str(total_no[ num-1 ]))
        print("longest row of " + str(num) + " apperd = " + str(longest_row[ num-1 ]))
    print("final flip = "+str(final_role))

One_M_rols()
display()
