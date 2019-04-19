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

    def add(self, x):
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
        return result_object, BigInteger.convert_to_str(result)

    @staticmethod
    def fill_with_zeroes(string, length):
        return string.zfill(length)

    def subtract(self, x):
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
        return result_object, BigInteger.convert_to_str(result)

    @staticmethod
    def split_string(string, len_of_num):
        str1 = BigInteger('')
        str2 = BigInteger('')
        for i in range(len_of_num):
            if i < len_of_num / 2:
                str1.a_number += string[i]
            else:
                str2.a_number += string[i]
        return str1, str2

    def multiplying(self, x):
        """number has a form : BigNumber1 = high1*B**len(object.a_number) + low1"""
        self_len = len(self.a_number)
        len_x = len(x.a_number)
        if self_len < 3 or len_x < 3:
            string_result = str(int(self.a_number) * int(x.a_number))
            result = BigInteger(string_result)
            return result
        print(str(10 ** (len(self.a_number))))
        high1, low1 = BigInteger.split_string(self.a_number, len(self.a_number))
        high2, low2 = BigInteger.split_string(x.a_number, len(x.a_number))

        z0 = low1.multiplying(low2)

        z1 = (low1.add(high1)[0]).multiplying(low2.add(high2)[0])

        z2 = high1.multiplying(high2)

        print(str(10 ** (len(self.a_number))))
        tmp_mul1 = BigInteger(str(10 ** (len(self.a_number))))
        tmp_mul2 = BigInteger(str(10 ** (len(self.a_number) // 2)))
        return z2.multiplying(tmp_mul1).add(((z1.subtract(z2)[0].subtract(z0))[0].multiplying(tmp_mul2).add(z0)[0]))

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
    big_number1 = make_random_string(100, 9)
    big_number2 = make_random_string(100, 9)
    x1 = BigInteger(big_number1)
    x2 = BigInteger(big_number2)

    "printing"
    print('x1 =         ', end='')
    x1.printing()
    print('x2 =         ', end='')
    x2.printing()

    "adding"
    print('adding:     ', x1.add(x2))

    "subtracting"
    print('subtracting:', x1.subtract(x2))

    "multiplying"
    print('multiplying:', x1.multiplying(x2))

    "factorial"
    # print('factorial: ', x1.factorial())


main()


