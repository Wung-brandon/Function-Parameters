#prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        print(i)
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('Its a prime number')
    else:
        print('its not a prime number')
            
prime_checker(number=9)