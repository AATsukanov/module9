#import matplotlib.pyplot as plt
import math

def memorize_func_dec(func):
    mem = {}

    def wrapper(*args):
        if not args in mem:
            mem[args] = func(*args)
        return mem[args]

    return wrapper


@memorize_func_dec
def compute_exp(n, p):
    if n == 0:
        return 0
    return (1 + 1 / n) ** (n * p)

def main():
    nn = [2**_ for _ in range(10)]
    p = 1
    for n in nn:
        print(f'{n}: {compute_exp(n, p):.5f} Δ = {(compute_exp(n, p) - math.exp(1))/math.exp(1)*100:.3f} %')

if __name__ == '__main__':
    main()