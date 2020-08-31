"""
Practice Problem 4
The next Palindrome
a palindrome is a string which when reversed is eqal to itself
Ex of Palindrome 616,mom,676,1000001

Problem - You have to take a number as a input from the user.you have to find
the next palindrome corresponding .Your first input should be number of cases and then takes all the cases
as input from the user

Input-
3

451
10
2133

Output - 
Next Palindrom for 451 is 454
Next Palindrom for 10 is 11
Next Palindrom for 2133 is 2222

"""


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":

    n = int(input("Enter the number of the test cases"))

numbers = []

for i in range(n):
    number = int(input("Enter the number :\n"))
    numbers.append(number)
# print(numbers)

for i in range(n):
    print(
        f"next palindrome for {numbers[i]} is {next_palindrome(numbers[i])} ")
