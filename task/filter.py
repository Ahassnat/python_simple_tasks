gs=['A','B','C','D','E']
def f_result(gs):
    return gs!='E'
gs_f=[]
for g in gs:
    if g!='E':
        gs_f.append(g)
print(gs_f)
# use comperhinstion التبسيط
print([g for g in gs if g!='E'])
# use filter function --- just here we use the function f_result ###
print(list(filter(f_result,gs)))

###use lambda
x=[1,2,3,4,5,6,7]
print(list(map(lambda n:n*n,x)))
