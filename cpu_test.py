    import itertools

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for divisor in range(3, n, 2):
            if n % divisor == 0:
                return False
        return True


    def find_next_prime(n):
        for val in itertools.count(n + 1):
            if is_prime(val):
                return val


    print(find_next_prime(154928599))