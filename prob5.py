import unittest


def getDivisibles(min, max):
    maximo = 1000000000
    respuesta = max
    # for i in range(min, max):
    #     maximo *= i
    while respuesta < maximo:
        for i in range(min, max):
            valido = True
            if respuesta % i != 0:
                valido = False
                break
        if valido:
            return respuesta
        respuesta += max

class Prob5TestCase(unittest.TestCase):
    def test(self):
        # Given
        min = 1
        max = 10
        # When
        answer = getDivisibles(min, max)
        # Then

        self.assertEqual(answer, 2520)

print(getDivisibles(1, 20))

# 232792560

# I can also use prime factoring such as
# 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19 == answer
