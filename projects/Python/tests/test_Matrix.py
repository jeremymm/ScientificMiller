from unittest import TestCase
from linear_algebra import Matrix

class TestMatrix(TestCase):
    def test_set_identity(self):
        number_of_rows = 3
        number_of_columns = 3
        test_matrix = Matrix.Matrix(number_of_rows, number_of_columns)
        test_matrix.set_identity()
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):
                if row_index == column_index:
                    if test_matrix.matrix[row_index][column_index] != 1.0:
                        self.fail()



