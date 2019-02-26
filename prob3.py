import unittest

def primeFactors(numero):
    lista = list()
    i = 2
    while numero > 1:
        if numero % i == 0:
            numero /= i
            lista.append(i)
            i = 2
        else:
            i += 1
    return lista


class TestPrimeFactors(unittest.TestCase):

    def testFactors(self):

        # Given

        number = 13195

        # When

        primes = primeFactors(number)
        self.assertEqual(primes, [5, 7, 13, 29])


print(primeFactors(600851475143))

# anser is 6857
