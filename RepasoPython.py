#1
def multiplos(n):

    for multiplo in range(1,11):
        print(multiplo*n)


multiplos(4);
print("-----------------")
#2
def indefinido():

    for indef in range(10,21):
        print(indef)


indefinido()


print("-----------------")

#3

def temp(far):

    for num in range(0,121,10):

     celsius = (num-32)*(5/9)
     print(celsius)

temp(100)
