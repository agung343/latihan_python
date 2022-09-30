def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It's not prime number")

prime_checker(number=12)