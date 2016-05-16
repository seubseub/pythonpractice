import math
from random import randint

result =0
count =0
while result<3:
    a = raw_input('put your number in 0~3 which means 0 to Rock, 1 to Scissors, 2 to Paper to win computer >> ')
    a = int(a)
    b = randint(0,2)

    if a == b:
        print 'Draw'
        result = result

    elif a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0:
        print 'User Lose'
        result -=1

    elif a == 0 and b == 2 or a == 1 and b == 0 or a == 2 and b == 1:
        print 'User Win'
        result +=1

    count +=1
    print result
print 'You win!! in %d count!'%(count)