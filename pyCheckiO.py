from collections.abc import Iterable
from typing import List, Any


class PyCheckiOLessons():

    # Multiply (Intro)
    def mult_two(self, a: int, b: int) -> int:
        """
        This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO.
        If you want to know how to get the maximum out of using CheckiO,
        check out our blog post "From Basic to Advance usage".
        This mission is the easiest one.
        Write a function that will receive 2 numbers as input and it should return the multiplication of these
        2 numbers.

        Input: Two arguments. Both are of type int.

        Output: Int.
        """
        return a * b

    # First Word (simplified)
    def first_word(self, text: str) -> str:
        """
        You are given a string and you have to find its first word.
        The input string consists of only English letters and spaces.
        There aren’t any spaces at the beginning and the end of the string.
        
        Input: A string (str).

        Output: A string (str).
        """
        return text.split(" ")[0]

    # Is Even
    def is_even(self, num: int) -> bool:
        """
        Check if the given number is even or not. Your function should return True if the number is even,
        and False if the number is odd.

        Input: An integer (int).

        Output: Logic value (bool).
        """

        return (num % 2) == 0

    # Acceptable Password I
    def is_acceptable_password(self, password: str) -> bool:
        """
        The verification condition is:
        the length should be bigger than 6.
        
        Input: A string (str).

        Output: A logic value (bool).
        """
        return len(password) > 6

    # Number Length
    def number_length(self, value: int) -> int:
        """
        You have a non-negative integer. Try to find out how many digits it has.

        Input: A non-negative integer (int).

        Output: An integer (int).
        """
        return len(str(value))

    # Backward String
    def backward_string(self, val: str) -> str:
        """
        You should return a given string in reverse order.

        Input: A string (str).

        Output: A string (str).
        """

        return val[::-1]

    # The Most Frequent
    def most_frequent(self, data: list[str]) -> str:
        """
        You have a sequence of strings, and you’d like to determine the most frequently occurring string
        in the sequence. It can be the only one.

        Input: Non-empty list of string (str).

        Output: A string (str).
        """
        return max(data, key=data.count)

    # Sum Numbers
    def sum_numbers(self, text: str) -> int:
        """
        In a given text you need to sum the numbers while excluding any digits that form part of a word.
        The text consists of numbers, spaces and letters from the English alphabet.

        Input: A string (str).

        Output: An integer (int).
        """
        return sum(int(string) for string in text.split(' ') if string.isdigit())

    # End Zeros
    def end_zeros(self, number: int) -> int:
        """
        Try to find out how many zeros a given number has at the end.

        Input: A non-negative integer (int).

        Output: An integer (int).
        """
        # asd =[]
        # for i in reversed(str(a)):
        #     if i == '0':
        #         asd.append(i)
        #     else:
        #         break
        # return asd.count('0')
        return len(str(number)) - len(str(number).strip('0'))

    # All the Same
    def all_the_same(self, elements: List[Any]) -> bool:
        """
        In this mission you should check if all elements in the given sequence are equal.

        Input: List.

        Output: Logic value (bool).
        """
        # return False not in [elements[0] == element for element in elements]
        return len(set(elements)) <= 1

    # Easy Unpack
    def easy_unpack(self, elements: tuple) -> tuple:
        """
        One important thing worth pointing out is that you need to use index in order
        to extract elements from the tuple. Pay attention, index counting starts from 0, not from 1.
        Which means that if you need to get the first element from the tuple elements, you should do elements[0],
        and the second element is elements[1].

        Input: A tuple, at least 3 elements long.

        Output: A tuple.
        """
        return (elements[0], elements[2], elements[-2])

    # Count Digits
    def count_digits(self, text: str) -> int:
        """
        You need to count the number of digits in a given string.

        Input: String.

        Output: Integer.
        """
        # [symbol.isdigit() for symbol in text].count(True) # Mine
        # sum(map(str.isdigit, text)) - Speedy
        return sum(symbol.isdigit() for symbol in text)  # Clear

    # All Upper I
    def is_all_upper(self, text: str) -> bool:
        """
        Check if a given string has all symbols in upper case.
        If the string is empty or doesn't have any letter in it - function should return True.

        Input: A string (str).

        Output: A logic value (bool).
        """
        # return False not in [symbol.isupper() or symbol.isdigit() or symbol == '' for symbol in text.split(' ')] # Mine

        return text.upper() == text  # Clear & Speedy

    # Remove All Before

    def remove_all_before(self, items: list, border: int) -> Iterable:
        """
        For the illustration we have a sequence [1, 2, 3, 4, 5]
        and we need to remove all elements that go before 3 - which are 1 and 2.
        We have two edge cases here: (1) if a cutting element cannot be found, then the sequence shoudn't be changed.
        (2) if the sequence is empty, then it should remain empty.

        Input: List and the border element.

        Output: List or another Iterable (tuple, iterator, generator).
        """
        # return next((items[id:] for id, item in enumerate(items) if item == border), items) # Mine
        # return next((items[items.index(item):] for item in items if item == border), items) # Mine is advanced

        return items[items.index(border):] if border in items else items

    # Replace First
    def replace_first(self, items: list) -> Iterable:
        """
        In a given sequence the first element should become the last one.
        An empty sequence or with only one element should stay the same.

        Input: List.

        Output: List or another Iterable (tuple, iterator, generator).
        """
        # if items:                              # Mine
        #     items.append(items[0])
        #     items.remove(items[0])
        # return items

        # return [items[i] for i in range(1, len(items))] + [items[0]] if items else items # - chatGPT

        if len(items):  # Mine is advanced
            items.append(items.pop(0))
        return items

    # Max Digit
    def max_digit(self, value: int) -> int:
        """
        You have a number and you need to determine which digit in this number is the biggest.

        Input: A positive integer (int).

        Output: An integer 0-9 (int).
        """
        # return int(max(list(str(value))))

        return max(map(int, str(value)))  # Speedy


if __name__ == '__main__':
    pyCheckiO_lessons = PyCheckiOLessons()
    result = pyCheckiO_lessons.max_digit(388)  # 6
    print(result)
