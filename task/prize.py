prizes=[2,3,4,5,6]
d_prizes=[]
for prize in prizes:
    d_prizes.append(prize*2)
print(d_prizes)
################################################

d_prizes= [prize*2 for prize in prizes]
print(d_prizes)
################################################
num =[2,4,5,6,9]
sq_num=[n**2 for n in num]
print(sq_num)
#################Even Numbers####################################
elm=[1,2,3,4,5,6,7,8,9,10]
x_even=[]
for x in elm:
    if x % 2 == 0:
        x_even.append(x)
print(x_even)

#############$$$Even number################
x_even=[x for x in elm if(x%2==0)]
print(x_even)
#######Odd Number###########
x_odd=[x for x in elm if(x%2==1)]
print(x_odd)
