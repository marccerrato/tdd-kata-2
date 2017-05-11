import pytest

from fizzbuzz import fizzbuzz

@pytest.mark.parametrize('n', [1, 2, 4, 8, 11])
def test_fizzbuzz_with_normal_number_returns_same_number(n):
    assert fizzbuzz(n) == n

@pytest.mark.parametrize('n', [3, 6, 9, 12])
def test_fizzbuzz_with_multiple_of_three_returns_fizz(n):
    assert fizzbuzz(n) == 'fizz'

@pytest.mark.parametrize('n', [5, 10, 20, 25])
def test_fizzbuzz_with_multiple_of_five_returns_buzz(n):
    assert fizzbuzz(n) == 'buzz'

@pytest.mark.parametrize('n', [15, 30, 45, 60])
def test_fizzbuzz_with_multiple_of_three_and_five_returns_fizzbuzz(n):
    assert fizzbuzz(n) == 'fizz buzz'

@pytest.mark.parametrize('n', [7, 14, 28])
def test_fizzbuzz_with_multiple_of_seven_returns_pop(n):
    assert fizzbuzz(n) == 'pop'

@pytest.mark.parametrize('n', [21, 42, 84])
def test_fizzbuzz_with_multiple_of_three_and_seven_returns_fizzpop(n):
    assert fizzbuzz(n) == 'fizz pop'

@pytest.mark.parametrize('n', [35, 70, 140])
def test_fizzbuzz_with_multiple_of_five_and_seven_returns_buzzpop(n):
    assert fizzbuzz(n) == 'buzz pop'

@pytest.mark.parametrize('n', [3*5*7, 3*5*7*2])
def test_fizzbuzz_with_multiple_of_three_five_and_seven_returns_fizzbuzzpop(n):
    assert fizzbuzz(n) == 'fizz buzz pop'

@pytest.mark.parametrize('n', [1, 3, 5])
def test_fizzbuzz_with_custom_substitution_and_normal_number_returns_same_number(n):
    assert fizzbuzz(n, substitutions=((2, 'fuzz'),)) == n

@pytest.mark.parametrize('n', [2, 4, 6])
def test_fizzbuzz_with_custom_substitution_and_matching_number_returns_substitution(n):
    assert fizzbuzz(n, substitutions=((2, 'fuzz'),)) == 'fuzz'

@pytest.mark.parametrize('n', [6, 12, 18])
def test_fizzbuzz_with_multiple_custom_substitution_and_matching_number_returns_substitution(n):
    assert fizzbuzz(n, substitutions=((2, 'fuzz'), (3, 'bizz'))) == 'fuzz bizz'
