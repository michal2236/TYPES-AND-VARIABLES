import random
computerThrow = random.randint(1,6)
userNumber = int(input("Co wyrzucił komputer?"))
if computerThrow == userNumber:
    print(True)
else:
    print(False)