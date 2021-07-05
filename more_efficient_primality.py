import math

number = input("Enter a number to check primality ")
while (not number.isdigit() or int(number) <= 1):
    print("Enter an actual number, and make sure it is > 1")
    number = input("Enter a number to check primality ")

number = int(number)
sqt = math.floor(math.sqrt(number))

# Factor mod 10
possible_factors_mod10 = range(10)
actual_factors = set()

if number % 2 == 1:
    # Odd numbers mod 10 only have odd factors
    possible_factors_mod10 = [1, 3, 5, 7, 9]


for i in possible_factors_mod10:
    for j in possible_factors_mod10:
        if (i * j) % 10 == number % 10:
            actual_factors.add(i)
            actual_factors.add(j)

possible_factors = set()
for i in range(2, sqt + 1):
    if (i % 10) in actual_factors:
        possible_factors.add(i)

prime = True
for i in possible_factors:
    if (number % i == 0):
        print(str(number) + ' is not prime, ' + str(i) + ' is a factor')
        prime = False
        break

if (prime):
    print(str(number) + ' is prime')

