# Score input
score = int(input('Score: '))
name = input('Insert your name: ')

#Grade calculation
print("Name is " + name)
if score > 79:
    print('The score is :  {}  :  Grade : A'.format(score))
elif score > 74:
    print('The score is :  {}  :  Grade : B+'.format(score))
elif score > 70:
    print('The score is :  {}  :  Grade : B'.format(score))
elif score > 64:
    print('The score is :  {}  :  Grade : C+'.format(score))
elif score > 59:
    print('The score is :  {}  :  Grade : C'.format(score))
elif score > 54:
    print('The score is :  {}  :  Grade : D+'.format(score))
elif score > 49:
    print('The score is :  {}  :  Grade : D'.format(score))
else:
    print('The score is :  {}  :  Grade : F'.format(score))
