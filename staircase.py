def staircase(n):
    if (n%2 == 0 and n > 0 and n <= 100):
        for stairs in range(1, n + 1):
            print(' ' * (n - stairs) + '#' * stairs)

staircase(4)