"""
Function that checks if a certain number is prime or not
"""
def checkForPrimes(value):
    for n in range(2,value):
        if value%n == 0:
            print(value,"is not a prime number. ",value,"is divisable by ",n)
            break
        elif n == value-1:
            print(value,"is prime")     
checkForPrimes(177)