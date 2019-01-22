from itertools import product,zip_longest,chain,permutations
from fractions import Fraction as Fr
import time

brackets=([(0, 4),(2, 6),(4, 8),(0, 6),(2, 8),(0, 4, 6, 10), (0, 5,1, 8), (0, 7,3, 8), (2, 7,3, 10), (2, 9,5, 10)])
brackets2=([(0, 4, 6, 10), (0, 4,1, 8), (0, 6,3, 8), (2, 6,3, 10), (2, 8,5, 10)])

def getDigits():
    user_input = input('Input 4 numbers : ')
    return user_input.split(' ')

def addFrac(X):
    return 'Fr('+X+')'

def solveSolution(digits):
    solved=False
    solution=0
    perm_digits=set(permutations(digits))
    perm_ops=list(product('+-*/', repeat=3))
    for perm_digit in perm_digits:
        for ops in perm_ops:
            if ('/' in ops):
                temp_digit=list(map(lambda X:addFrac(X),perm_digit))
            else:
                temp_digit=perm_digit
            exp=list(chain.from_iterable(zip_longest(temp_digit,ops,fillvalue='')))
            for bracket in brackets2:
                exp_temp=exp.copy()
                for indexinsert,brac in zip(bracket,'()()'):
                    exp_temp.insert(indexinsert,brac)
                exp_txt=''.join(exp_temp)
                try:
                    result=eval(exp_txt)
                except:
                    continue
                if result==24:
                    solution+=1
                    solved=True
                    print(exp_txt)                
    if not solved:
        print('No solution found.')
    else:
        print('Found',solution,'solutions.')
        
digits=getDigits()
start=time.time()
solveSolution(digits)
end=time.time()
print('Time Execution : ',end-start,'s')
