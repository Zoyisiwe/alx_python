#!/usr/bin/env python3
 #fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_numbers = [0, 1]
        while len(fib_numbers) < n:
            next_num = fib_numbers[-1] + fib_numbers[-2]
            fib_numbers.append(next_num)
        return fib_numbers