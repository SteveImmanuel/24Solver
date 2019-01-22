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

def operate(digit1,op,digit2):
    if op=='+':
        return float(digit1)+float(digit2)
    elif op=='-':
        return float(digit1)-float(digit2)
    elif op=='*':
        return float(digit1)*float(digit2)
    elif op=='/':
        return float(digit1)/float(digit2)

def makeExp(perm_digit,ops,variation):    
    if variation==1:
        result=['('+perm_digit[0]+ops[0]+perm_digit[1]+')'+ops[1]+'('+perm_digit[2]+ops[2]+perm_digit[3]+')']
        result.append(operate(operate(perm_digit[0],ops[0],perm_digit[1]),ops[1],operate(perm_digit[2],ops[2],perm_digit[3])))
    elif variation==2:
        result=['(('+perm_digit[0]+ops[0]+perm_digit[1]+')'+ops[1]+perm_digit[2]+')'+ops[2]+perm_digit[3]]
        result.append(operate(operate(operate(perm_digit[0],ops[0],perm_digit[1]),ops[1],perm_digit[2]),ops[2],perm_digit[3]))
    elif variation==3:
        result=['('+perm_digit[0]+ops[0]+'('+perm_digit[1]+ops[1]+perm_digit[2]+'))'+ops[2]+perm_digit[3]]
        result.append(operate(operate(perm_digit[0],ops[0],operate(perm_digit[1],ops[1],perm_digit[2])),ops[2],perm_digit[3]))
    elif variation==4:
        result=[perm_digit[0]+ops[0]+'(('+perm_digit[1]+ops[1]+perm_digit[2]+')'+ops[2]+perm_digit[3]+')']
        result.append(operate(perm_digit[0],ops[0],operate(operate(perm_digit[1],ops[1],perm_digit[2]),ops[2],perm_digit[3])))
    else:
        result=[perm_digit[0]+ops[0]+'('+perm_digit[1]+ops[1]+'('+perm_digit[2]+ops[2]+perm_digit[3]+'))']
        result.append(operate(perm_digit[0],ops[0],operate(perm_digit[1],ops[1],operate(perm_digit[2],ops[2],perm_digit[3]))))
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
                try:
                    result=makeExp(perm_digit,ops,i)
                except:
                    continue
                if abs(result[1]-24)<=epsilon:
                    solutions.append(result[0])              
    end=time.time()
    solutions=sorted(solutions)
    for solution in solutions:
        print(solution)
    print('Found',len(solutions),'solution(s).')
    print('Time Execution :',end-start,'s')
