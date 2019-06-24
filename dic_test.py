def showspace(sp):
    for n,tw in sp.items():
        print(f'the name is : {n} : the space ofthe home is : {tw}')

def space(t,w):
    return t*w
home_space={}
while True:
    name=input('name of owner')
    tallof=int(input('enter the tall of home'))
    widthof=int(input('enter the width : '))
    spaceof=space(tallof,widthof)
    home_space[name]=spaceof

    another= input('anter home y/n :: ')
    if another=='y':
        continue
    else:
        break
showspace(home_space)
