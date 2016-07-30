__author__ = "Jeremy Michael Miller"
__copyright__ = "Copyright 2016, Scientific Miller"
__credits__ = ["Jeremy Michael Miller"]
__license__ = "Fair use v0.9"
__version__ = "0.0.1"
__maintainer__ = "Jeremy Michael Miller"
__email__ = "maybe_later@mst.dnsalias.net"
__status__ = "Alpha"


class Matrix:
    """A matrix class that is row major and implements basic matrix linear_algebra operations
    Row major was chosen to match NumPy if used and if this class interfaces the C/C++
    implementation of a matrix object."""

    def __init__(self, number_of_rows, number_of_columns):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns;
        self.matrix = [[0 for i in range(self.number_of_rows)] for j in range(self.number_of_columns)]

    def __check_range(self, index):
        if index < self.number_of_rows * self.number_of_columns:
            range_ok = True
        else:
            raise ValueError("Index is out of range for this matrix.")
        return range_ok

    def __check_dimensions(self, matrix):
        if self.number_of_rows != matrix.number_of_rows or \
                        self.number_of_columns != matrix.number_of_columns:
            raise ValueError(
                "When adding two matrices together the number of rows and columns in both matrices must be equal.")

    def set_identity(self):
        for row_index in range(self.number_of_rows):
            for column_index in range(self.number_of_columns):
                if row_index == column_index:
                    try:
                        self.matrix[row_index][column_index] = 1.0
                    except IndexError:
                        pass

    def get(self, row_index, column_index):
        if row_index < self.number_of_rows and column_index < self.number_of_columns:
            index = row_index * column_index
            return_value = self.matrix[index]
        else:
            raise ValueError("Either row_index or column index is out of range for this matrix.")
        return return_value

    def get(self, index):
        if self.__check_range(self, index):
            return_value = self.matrix[index]
        return return_value

    def addition(self, matrix):
        if self.__check_dimensions(matrix):
            for row_index in range(self.number_of_rows):
                for column_index in range(self.number_of_columns):
                    index = row_index * column_index
                    self.matrix[index] = self.matrix[index] + matrix.get(index)

