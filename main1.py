'''
Functie care verifica daca un numar n este prim
'''
def is_prime(n):
    nr = 0
    for x in range(1, n+1):
        if n % x == 0:
            nr = nr + 1
    if nr == 2:
        return True
    else:
        return False

'''
Functia test verifica daca functia pentru numar prim este corecta
'''
def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(2) == True
    assert is_prime(1) == False
    assert is_prime(9) == False
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(23) == True
    assert is_prime(27) == False
    assert is_prime(81) == False
    assert is_prime(16) == False

def get_largest_prime_below(n):
    '''

    :param n:
    :return:
    numarul este format in variabila prim
    '''
    prim = n - 1
    while prim > 1:
        if is_prime(prim) == True:
            return prim
        else:
            prim = prim - 1

def test_get_largest_prime_below():
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(7) == 5
    assert get_largest_prime_below(12) == 11
    assert get_largest_prime_below(26) == 23
    assert get_largest_prime_below(45) == 43
    assert get_largest_prime_below(60) == 59

def main():
    n = int(input('Introduceti un numar: '))
    print(f'Ultimul numar prim mai mic decat {n} este {get_largest_prime_below(n)}')

test_is_prime()
test_get_largest_prime_below()
main()

