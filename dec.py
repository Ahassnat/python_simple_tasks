def showMark(marks):
    for s,m in marks.items():
        print(f'the student name{s} and his mark is{m}')

std_mark={}
while True:
    std=input('enter the name : ')
    mark=input('enter th mark : ')
    std_mark[std]=mark

    another=input('do you need to enter another student(y/n) : ')
    if another=='y':
        continue
    else:
        break
showMark(std_mark)
