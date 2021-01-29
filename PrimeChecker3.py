import math


def main():
    test_number = int(input("Please enter the number that you wish to test \n"))

    test_factor = 2  # Initializes 2 as the first test case, since we don't need to test 1
    test_limit = test_number
    factor_amount = 0  # This number indicates the amount of factor that the test number has
    factors = [1,
               test_number]  # 1 and the test number is included because all ints are divisible by 1 and itself

    while test_factor < test_limit:
        if test_number % test_factor == 0:
            factors.append(test_factor)
            test_limit = test_number / test_factor  # Test limit is also a factor
            factors.append(int(test_limit))
        else:
            test_limit = math.ceil((
                                               test_number / test_factor))  # Eliminates numbers that could not possibly be factors

        test_factor += 1  # Moves on to the next test factor

    for i in factors:
        factor_amount += 1

    factors.sort()

    print(factors)
    print("The number that you entered has " + str(factor_amount) + " factors")

    if factor_amount == 2:
        print("Your number is a prime number")
    else:
        print("Your number is not a prime number")


if __name__ == "__main__":
    main()