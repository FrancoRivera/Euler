import unittest

def getDifference(min, max):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(min, max+1):
        sum_of_squares += (i*i)
        square_of_sum += i
    square_of_sum *= square_of_sum

    return square_of_sum - sum_of_squares

class Prob6TestCase(unittest.TestCase):
    def test(self):
        # Given
        min = 1
        max = 10
        # When
        answer = getDifference(min, max)
        # Then
        self.assertEqual(answer, 2640)

print(getDifference(1, 100))

# Answer: 25164150
# Can Also use mathematic formulas
