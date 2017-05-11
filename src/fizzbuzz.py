
DEFAULT_SUBSTITUTIONS = (
    (3, 'fizz'),
    (5, 'buzz'),
    (7, 'pop'),
)

def fizzbuzz(n, substitutions=None):
    result = []

    if substitutions is None:
        substitutions = DEFAULT_SUBSTITUTIONS

    for divisor, word in substitutions:
        if n % divisor == 0:
            result.append(word)

    if result:
        return ' '.join(result)

    return n