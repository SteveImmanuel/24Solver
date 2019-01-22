import time

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

def makeExp(perm_digit,ops,variation):
    if variation==1:
        result='('+perm_digit[0]+ops[0]+perm_digit[1]+')'+ops[1]+'('+perm_digit[2]+ops[2]+perm_digit[3]+')'
    elif variation==2:
        result='(('+perm_digit[0]+ops[0]+perm_digit[1]+')'+ops[1]+perm_digit[2]+')'+ops[2]+perm_digit[3]
    elif variation==3:
        result='('+perm_digit[0]+ops[0]+'('+perm_digit[1]+ops[1]+perm_digit[2]+'))'+ops[2]+perm_digit[3]
    elif variation==4:
        result=perm_digit[0]+ops[0]+'(('+perm_digit[1]+ops[1]+perm_digit[2]+')'+ops[2]+perm_digit[3]+')'
    else:
        result=perm_digit[0]+ops[0]+'('+perm_digit[1]+ops[1]+'('+perm_digit[2]+ops[2]+perm_digit[3]+'))'
    return result

if __name__=='__main__':
    user_input = input('Input 4 numbers : ')
    digits=user_input.split(' ')
    start=time.time()
    solutions=[]
    epsilon=1e-12
    for perm_digit in generatePerm(digits):
        for ops in generateOps():
            for i in range(1,6):
                exp_txt=makeExp(perm_digit,ops,i)
                try:
                    result=eval(exp_txt)
                except:
                    continue
                if abs(result-24)<=epsilon:
                    solutions.append(exp_txt)               
    end=time.time()
    for solution in solutions:
        print(solution)
    print('Found',len(solutions),'solution(s).')
    print('Time Execution :',end-start,'s')