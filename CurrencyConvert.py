numOfBath = float(input("Enter number (Thai Bath) :  "))
currency = int(input("Enter (1 - 3) exchange TH bath to (1 is US dollar : 2 is Yen : 3 is HK Dollar)"))
if currency == 1:
    result = numOfBath/34.11
    print("{} TH bath can convert to {} US dollar".format(numOfBath,result))
elif currency == 2:
    result = (numOfBath*100)/25.97
    print("{} TH bath can convert to {} Yen".format(numOfBath, result))
elif currency == 3:
    result = numOfBath/4.35
    print("{} TH bath can convert to {} HK dollar".format(numOfBath, result))
else:
    print("you put wrong currency conversion")