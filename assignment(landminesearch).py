import math
from random import randint

n = int(raw_input('num that determine size of mape : '))




Bomb_count = 0

m = randint(int(n)/2 + 1,int(n)**2-1)

temp = int(m)

total = int(n)**2


Remain_bomb = 0
r = [[]]

x = '#'
a = '#'
r = [[x for i in range(int(n))] for i in range(int(n))]
a = [[a for i in range(int(n))] for i in range(int(n))]

for i in range(int(n)):
    print r[i]

print '***********************************************'




while m!=0:
    x = randint(0,int(n)-1)
    y = randint(0,int(n)-1)
    a[x][y] = '*'
    m -= 1

m = temp

print  m
for i in range(int(n)):
    print a[i]


def Open(x,y):
    global a,n,total,m,Remain_bomb
    if x< 0 or x> n or y < 0 or y > n:
        print 'Value is out of range!'
        return 1
    if a[x][y] == '*':
        global Bomb_count
        Bomb_count = 1
        return 0


    else:
        r[x][y] = ' '
        total -= 1
        for i in range(n):
            print r[i]
        print '**************'
        if x - 1 >= 0:
            if a[x-1][y] == '*':
                r[x-1][y] = '#'
                if m == total:
                    Remain_bomb = 1
        if x - 1 >= 0:
            if a[x-1][y] == '#':
                if r[x-1][y] == '#':
                    r[x-1][y] = ' '
                    total -= 1
                    if m == total:
                        Remain_bomb = 1
                    for i in range(n):
                        print r[i]
                    print '**************'
                    Open(x-1,y)
        if y - 1 >= 0:
            if a[x][y-1] == '*':
                r[x][y-1] = '#'
                if m == total:
                    Remain_bomb = 1
        if y - 1 >= 0:
            if a[x][y - 1] == '#':
                if r[x][y-1] == '#':
                    r[x][y - 1] = ' '
                    total -= 1
                    if m == total:
                        Remain_bomb = 1
                    for i in range(n):
                        print r[i]
                    print '**************'
                    Open(x,y-1)
        if x + 1 < n:
            if a[x+1][y] == '*':
                r[x+1][y] = '#'
                if m == total:
                    Remain_bomb = 1
        if x + 1 < n:
            if a[x+1][y] == '#':
                if r[x+1][y] == '#':
                    r[x+1][y] = ' '
                    total -= 1
                    if m == total:
                        Remain_bomb = 1
                    for i in range(n):
                        print r[i]
                    print '**************'
                    Open(x+1,y)

        if y + 1 < n :
            if a[x][y+1] == '*':
                r[x][y+1] = '#'
                if m == total:
                    Remain_bomb = 1
        if y + 1 < n:
            if a[x][y + 1] == '#':
                if r[x][y+1] == '#':
                    r[x][y + 1] = ' '
                    total -= 1
                    if m == total:
                        Remain_bomb = 1
                    for i in range(n):
                        print r[i]
                    print '**************'
                    Open(x,y+1)




    return 0

while Bomb_count!= 1:
        x,temp,y = raw_input('x,y : ')
        Open(int(x),int(y))

        for i in range(n):
            print r[i]

        print '***************************************'

        for i in range(n):
            print a[i]

if Remain_bomb ==  1:
    print 'Remain Only Bomb'

if Bomb_count == 1:
    print 'Bomb burst!!'
