import math

'''
print 'hi'

a = 10
print a
b = 15
c = a + b
print c

name = 'yong'
sentance = 'My name is '
print sentance, name
print sentance + name
sentance = sentance + name
print sentance




a = 3
b = 4

c= math.sqrt(a**2 + b**2)

print c
'''
a = 1
b = 2
c = 1

x1= (-b + math.sqrt(b**2-4*a*c))/2*a
x2= (-b - math.sqrt(b**2-4*a*c))/2*a

print x1 , x2
'''
value = 'hello'
print value[1:-1]

value2 = 'hello world'
value3 = 'python'
value4 = 'hello ' + value3 + ' world'

print len(value2)
print value2[:5]
print value2[6:]
print 'hello ' + value3 + ' world'
print value4

a = raw_input('a >> ')
a = int(a)
b = raw_input('b >> ')
b = int(b)
c = raw_input('c >> ')
c = int(c)

x1 = (-b + math.sqrt(b**2 -4*a*c))/2*a
x2 = (-b - math.sqrt(b**2 -4*a*c))/2*a

print x1, x2


if (b**2)-(4*a*c)<0:
    print 'no answer'
elif (b**2)-(4*a*c) ==0:
    print x1 or x2
else :
    print x1, x2



a = raw_input('a >> ')
a = int(a)
i= 0

while i<9:
    print '%d x %d = %d'%(a,i+1,a*(i+1))
    i += 1

a = raw_input('a >> ')
a = int(a)
i= 0
while a-i !=0:
    print (' '*(a-i-1)) + ('*'*(i*2+1))
    i +=1

a= raw_input('a>> ')
a= int(a)
i = 0

while i<9 :

    print('%d x %d = %d'%(a,i+1,a*(i+1)))
    i+=1


a = raw_input('a>> ')
a = int(a)
i = 0

for i in range(0,9):
    print('%d x %d = %d'%(a,i+1,a*(i+1)))


from random import randint
result =0
count =0
while result<3:
    a = raw_input('put your number in 0~3 to win computer >> ')
    a = int(a)
    b = randint(0,3)
    if a>b:
        result +=1
    elif a<b:
        result -=1
    else:
        result = result
    count +=1
    print result

print 'You win!! in %d count!'%(count)
'''

nums = range(1,11)
i=0
while i<len(range(1,11)):
    print nums[i]
    i+=1

nums = [10, 30, 20, 40]
for num in nums:

    print num

'''
print range(0,7,2)


a = raw_input('a ==')
a = int(a)

for i in range(0,9):
    print '%d * %d = %d'%(a,i+1,a*(i+1))

list = range(1,5)
num = [x**2 for x in [1,2,3]]

print num


odd_num = [x**2 for x in [1,2,3] if(x % 2 == 2 )]

print odd_num


dictionary = {'key' : 'value', 123 : 'asdf', (1,2) : 123}

print dictionary['key']


users = {'yong' : '010292142121521'}

for key in users.keys():
    print key, users[key]

for key, value in users.iteritems():
    print key, value



def qurdaritc_formula(a,b,c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2=  (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a

    if (b ** 2) - (4 * a * c) < 0:
        return ()
    elif (b ** 2) - (4 * a * c) == 0:
        return x1
    else (b**2)-4 * a * c > 0:
        return x2 x1, x2

a = raw_input('a >>')
b = raw_input('b >>')
c = raw_input('c >>')
qurdaritc_formula(a,b,c)

print type(f)
multiply_add = lambda x,y,z = (x+y)*c

print multiply_add(10, y= 10)
'''

import scrapy