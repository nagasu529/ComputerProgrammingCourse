"""
a =[]
for i in range(5):
    a.append(i)

b = []
for i in range (5):
    i = 2
    b.append(i)

#print(a)
#print(b)

def factorial(x):
    result = []
    for i in range(x + 1):
        result.append(i)
    print(result)
    print('factorial result is {}'.format(sum(result)))
factorial(3)
 """       

def countdown(n):
    while n > 0:
        print(n)
        n  = n-1
    print('blase off')

#countdown(10)


"""
n = 10
while n > 0:
    print(n)
    n = n-1
print('blast off')
"""


x = 3
ans = 0
itersLeft = x
while (itersLeft != 0): 	# Square an integer, the hard way
    #print(ans)
    if ans == 0:
        ans = ans + x
    else:
        ans = ans * itersLeft
    itersLeft = itersLeft - 1   
print(str(x) + ' * ' + str(x) + ' = ' + str(ans))
