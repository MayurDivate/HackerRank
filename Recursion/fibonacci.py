
def fibonacci_serise(n):
    if n < 1:
        return n
    else:
        return fibonacci_serise(n-1) + fibonacci_serise(n-2)

print(fibonacci_serise(3))