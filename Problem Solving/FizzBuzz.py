# PROBLEM 1 (Beginner): FizzBuzz
# Return a list of numbers from 1 to n. For multiples of 3 use "Fizz",
# for multiples of 5 use "Buzz", for multiples of both use "FizzBuzz".
# ---------------------------------------------------------------
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

print(fizzbuzz(15))