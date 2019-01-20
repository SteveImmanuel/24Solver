import time
from fractions import Fraction as f

brackets=([(0,4,6,10),(0,4,1,8),(0,6,3,8),(2,6,3,10),(2,8,5,10)])

def getDigits():
    user_input = input('Input 4 numbers : ')
    return user_input.split(' ')

def generatePerm(L):
    if len(L)==0:
        return set()
    elif len(L)==1:
        return [(L[0],)]
    else:
        result=set()
        for i in range(0,len(L)):
            first=(L[i],)
            L_rem=L[:i]+L[i+1:]
            for tempres in generatePerm(L_rem):
                result.add(first+tempres)
        return result    

def generateOps():
    op='+-*/'
    result=[]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result.append([op[i]]+[op[j]]+[op[k]])
    return result

def tupleList(L1,L2,over):
    result=[]
    shorter=len(L1)<len(L2)
    for i in range(min(len(L1),len(L2))):
        result.append((L1[i],L2[i]))
    if over:
        if shorter:
            for i in range(len(L1),len(L2)):
                result.append(('',L2[i]))
        else:
            for i in range(len(L2),len(L1)):
                result.append((L1[i],''))
    return result

def removeTuple(L):
    result=[]
    for i in L:
        for j in i:
            result.append(j)
    return result

def solveSolution(digits):
    solved=False
    solution=0
    for perm_digit in generatePerm(digits):
        for ops in generateOps():
            if ('/' in ops):
                proc_digit=['f('+x+')' for x in perm_digit]
                division=True
            else:
                proc_digit=perm_digit
                division=False
            exp=removeTuple(tupleList(proc_digit,ops,True))
            for bracket in brackets:
                exp_temp=exp.copy()
                for indexinsert,brac in tupleList(bracket,'()()',False):
                    exp_temp.insert(indexinsert,brac)
                try:
                    result=eval(''.join(exp_temp))
                except:
                    continue
                if result==24:
                    solution+=1
                    solved=True
                    if division:
                        exp_temp=[x.replace('f(','').replace(')','') if x!=')' else x for x in exp_temp] 
                    exp_txt=''.join(exp_temp)
                    print(exp_txt)                
    if not solved:
        print('No solution found.')
    else:
        print('Found',solution,'solutions.')
        
if __name__=='__main__':
    digits=getDigits()
    start=time.time()
    solveSolution(digits)
    end=time.time()
    print('Time Execution : ',end-start,'s')