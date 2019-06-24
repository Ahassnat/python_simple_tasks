from random import shuffle

def jump(word):
    x=list(word)
    shuffle(x)
    return '-'.join(x)

months=['april','mars','january','febreary']
month_s=[]
####
#for m in months:
#    month_s.append(jump(m))

#print(month_s)
######
month_s=[jump(m) for m in months]
print(month_s)
