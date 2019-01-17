from itertools import product,zip_longest,chain,permutations
import time

brackets=([(0, 4),(2, 6),(4, 8),(0, 6),(2, 8),(0, 4, 6, 10), (0, 5,1, 8), (0, 7,3, 8), (2, 7,3, 10), (2, 9,5, 10)])
brackets2=([(0, 4, 6, 10), (0, 4,1, 8), (0, 6,3, 8), (2, 6,3, 10), (2, 8,5, 10)])
# [(0,1,5,8),(0,3,7,8)],(2,3,7,10),(2,5,9,10)]
def getDigits():
    user_input = input('Input 4 numbers : ')
    return user_input.split(' ')

def solveSolution(digits):
    solved=False
    perm_digits=list(permutations(digits))
    perm_ops=list(product('+-*/', repeat=3))
    for perm_digit in perm_digits:
        for ops in perm_ops:
            exp=list(chain.from_iterable(zip_longest(perm_digit,ops,fillvalue='')))
            for bracket in brackets2:
                exp_temp=exp.copy()
                for indexinsert,brac in zip(bracket,'()'*(len(bracket)//2)):
                    exp_temp.insert(indexinsert,brac)
                exp_txt=''.join(exp_temp)
                try:
                    result=eval(exp_txt)
                except:
                    # print('fail:',exp_txt)
                    continue
                if result==24:
                    solved=True
                    print(exp_txt)                
    if not solved:
        print('No solution found.')
        
digits=getDigits()
start=time.time()
solveSolution(digits)
end=time.time()
print('Time Execution : ',end-start,'s')