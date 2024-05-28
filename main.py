"""
This program calculates fibonacci number based on memoization
"""
def main():
    while True:
        try:
            user_number = int(input("Enter your number: "))
            if user_number < 0:
                print("Please enter a positive number")
            result = fibonacci_memo(user_number)
            print(result)
        except ValueError:
            print("Invalid input")


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1;
    memo[n] = fibonacci_memo(n - 2, memo) + fibonacci_memo(n - 1, memo)
    return memo[n]

main()

