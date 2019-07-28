from _1_find_primes import is_prime


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(7)
    assert is_prime(1223)
    assert is_prime(2659)