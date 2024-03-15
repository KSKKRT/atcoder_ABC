def sieve(n: int) -> bool:
    # is_prime[k] : 整数kが素数か否か
    is_prime: list[bool] = [True for _ in range(n+1)]
    is_prime[0], is_prime[1] = False, False

    for i in range(n+1):
        if is_prime[i]:
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    return is_prime[n]
    

if __name__ == '__main__':
    def print_prime(n: int) -> None:
        print(f'{n} is Prime!' if sieve(n) else f'{n} is not Prime.')

    n_list = [13, 42, 137, 205, 2027]
    for n in n_list:
        print_prime(n)
