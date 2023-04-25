def happyBirthdaySong(personName):
    print("")
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday to {}".format(personName))
    print("Happy birthday to you")

name = input("What's your name: ")
happyBirthdaySong(name)



def advHappyBirthday(occasion, personName):
    print("")
    print("Happy {} to you".format(occasion))
    print("Happy {} to you".format(occasion))
    print("Happy {} to {}".format(occasion,personName))
    print("Happy {} to you".format(occasion))

advHappyBirthday('monday', 'kitti')

def bmi_cal(name, weight, height):
    bmi = weight/height **2
    print('--Hello', name)
    print('Your BMI is  {}'.format(bmi))

print("BMI calculator")
name = input("Enter your name: ")
weight = float(input("Enter weight (kg.))"))
height = float(input("Enter height (cm.)"))

bmi_cal(name, weight, height)



