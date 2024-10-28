

# Create a program that prompts the user to enter a number n and then calculates and displays the sum of all odd numbers up to that number n.



def calculateSumOfOdd(n):
    if n < 1:
        return 0
    if n % 2 != 0:
        return n + calculateSumOfOdd(n-1)
    return calculateSumOfOdd(n-1)

user_input = int(input("Enter your number : "))
print( calculateSumOfOdd(user_input) )