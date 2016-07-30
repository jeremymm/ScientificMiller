import random
from unittest import TestCase
from linear_algebra import Matrix


class TestMatrix(TestCase):
    def test_set_identity(self):
        for number_of_rows in range(16):
            for number_of_columns in range(16):
                test_matrix = Matrix.Matrix(number_of_rows, number_of_columns)
                test_matrix.set_identity()
                for row_index in range(number_of_rows):
                    for column_index in range(number_of_columns):
                        if row_index == column_index:
                            if test_matrix.matrix[row_index][column_index] != 1.0:
                                self.fail(
                                    "Failed to set identity on a " + number_of_rows + " by " + number_of_columns + " matrix.")

    def test_addition(self):
        for number_of_rows in range(16):
            for number_of_columns in range(16):
                operand1 = Matrix.Matrix(number_of_rows, number_of_columns)
                operand2 = Matrix.Matrix(number_of_rows, number_of_columns)
                try:
                    operand1.addition(operand2)
                except ValueError:
                    self.fail()
                except IndexError:
                    self.fail()
