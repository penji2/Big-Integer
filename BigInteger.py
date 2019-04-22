import numpy as np
import random
import math


class BigInteger:
    def __init__(self, data):
        self.a_number = data

    @staticmethod
    def convert_to_str(array):
        # converting integer list to string list
        s = [str(i) for i in array]
        result = str("".join(s))
        return result

    def printing(self):
        print(self.a_number)

    def __add__(self, x):
        result = []
        guard = 0
        if len(x.a_number) < len(self.a_number):
            x.a_number = BigInteger.fill_with_zeroes(x.a_number, len(self.a_number))
        for i in range(len(self.a_number) - 1, - 1, -1):
            tmp = int(self.a_number[i]) + int(x.a_number[i])

            if tmp + guard < 10:
                result.append(tmp + guard)
                guard = 0
            else:
                result.append(tmp + guard - 10)
                guard = 1
        if guard == 1:
            result.append(guard)
        result.reverse()
        result_object = BigInteger(BigInteger.convert_to_str(result))
        return result_object

    @staticmethod
    def fill_with_zeroes(string, length):
        return string.zfill(length)

    def __sub__(self, x):
        result = []
        guard = 0
        if len(x.a_number) < len(self.a_number):
            x.a_number = BigInteger.fill_with_zeroes(x.a_number, len(self.a_number))
        for i in range(len(self.a_number) - 1, - 1, -1):
            tmp = int(self.a_number[i]) - int(x.a_number[i])

            if tmp - guard >= 0:
                result.append(tmp - guard)
                guard = 0
            else:
                result.append(tmp + 10 - guard)
                guard = 1
        result.reverse()
        result_object = BigInteger(BigInteger.convert_to_str(result))
        return result_object

    @staticmethod
    def split_string(string, len_of_num):
        str1, str2 = string[:len_of_num], string[len_of_num:]
        print('str1=', str1, 'str2=', str2)
        str1 = BigInteger(str1)
        str2 = BigInteger(str2)
        return str1, str2

    def __mul__(self, x):
        """number has a form : BigNumber1 = high1*B**len(object.a_number) + low1"""

        if len(x.a_number) < 4 or len(self.a_number) < 4:
            string_result = str(int(self.a_number) * int(x.a_number))
            result = BigInteger(string_result)
            return result

        m = min(len(self.a_number), len(x.a_number))
        # print(m)
        m2 = m // 2
        # print(m2)

        high1, low1 = BigInteger.split_string(self.a_number, m2)
        high2, low2 = BigInteger.split_string(x.a_number, m2)

        z0 = low1 * low2  # 213*222
        print('z0 = ')
        z0.printing()
        z1 = (low1 + high1) * (low2 + high2)  # (222 + 209) * (111 + 213)
        print('z1 = ')
        z1.printing()
        z2 = high1 * high2  # 209 * 111
        print('z2 = ')
        z2.printing()

        tmp_mul1 = BigInteger(str(10 ** m2 * 2))
        tmp_mul2 = BigInteger(str(10 ** m2))
        # print('TEST')
        # (z1 - z2 - z0).printing()
        result = (z2 * tmp_mul1) + (((z1 - z2) - z0) * tmp_mul2) + z0
        return result

    def factorial(self):
        unit = BigInteger('1')
        if self.a_number == unit:
            return unit

        return self.multiplying((self.subtract(unit)[0]).factorial())


def testing(x):
    if x == 0:
        return 1
    return x * testing(x - 1)

    pass


def make_random_string(length_of_table, max_number):
    random_table = np.random.randint(1, max_number, length_of_table)
    string = BigInteger.convert_to_str(random_table)
    return string


def main():
    big_number1 = make_random_string(4, 9)
    big_number2 = make_random_string(4, 9)
    # x1 = BigInteger(big_number1)
    # x2 = BigInteger(big_number2)

    x1 = BigInteger('209222')
    x2 = BigInteger('111213')

    "printing"
    print('x1 =         ', end='')
    x1.printing()
    print('x2 =         ', end='')
    x2.printing()

    "adding"
    print('adding:     ', end='')
    (x1 + x2).printing()

    "subtracting"
    print('subtracting: ', end='')
    (x1 - x2).printing()
    "multiplying"
    print('multiplying: ', end='')
    (x1 * x2).printing()
    "factorial"
    # print('factorial: ', x1.factorial())


main()


