import function
import pytest



def test_find_primes():
    assert  function.find_primes(10)=={1, 2, 3, 5, 7}


@pytest.mark.parametrize("end ,result",[(2, {0,1}),(5,{0,1,3})])
def test_find_primes(end,result):
    assert function.find_primes(end) == result



def test_find_primes_0():
    assert  function.find_primes(0) == set()

def test_find_primes_faild():
    assert  function.find_primes(12) == set()

def test_find_primes_negative():
    assert  function.find_primes(-5) ==set()


def test_sort_list():
    assert  function.sort_list([4,5,8,9,1])==[1,4,5,8,9]

def test_sort_list_faild():
    assert  function.sort_list([]) ==[1,2]

