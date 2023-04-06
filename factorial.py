# Factorial 3 value

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

print("{} factorial value is {}".format(x, ans))