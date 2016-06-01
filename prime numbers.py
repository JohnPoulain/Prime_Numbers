#create a list of 2 to the user input
to_check = list(range(2,(int(input ("how high do you want to check for primes? "))+1)))

def check_numbers(checkable):
    """removes all numbers that checkable goes into except itself"""
    i = 0
    while i < (len(to_check)):
        if (to_check[i] % checkable) == 0 and (to_check[i] - checkable) != 0:
            del to_check[i]
        i += 1
    return(to_check)

i = 0
while i < (len(to_check)):
    check_numbers(to_check[i])
    i += 1
input (to_check)
