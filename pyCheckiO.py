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

    # Beginning Zeros
    def beginning_zeros(self, a: str) -> int:
        """
        You have a string that consist only of digits.
        You need to find how many zero digits ("0") are at the beginning of the given string.

        Input: A string (str), that consists of digits.

        Output: An integer (int).
        """

        # zoro_list = []     # Mine
        # for digit in a:
        #     if digit == '0':
        #         zoro_list.append(digit)
        #     else:
        #         break
        #
        # return len([digit for digit in a if digit == '0'])

        # str_int = str(int(a))  # Creative
        # return len(a) - len(str_int) + (str_int == '0')

        return len(a) - len(a.lstrip('0'))

    # Between Markers (simplified)
    def between_markers(self, text: str, start: str, end: str) -> str:
        """
        You are given a string and two markers (the initial one and final).
        You have to find a substring enclosed between these two markers. But there are a few important conditions.

        - The initial and final markers are always different.
        - The initial and final markers are always 1 char size.
        - The initial and final markers always exist in a string and go one after another.

        Input: Three arguments. All of them are strings (str).
        The second and third arguments are the initial and final markers.

        Output: A string (str).
        """

        return text.split(start)[-1].split(end)[0]

    # Split Pairs
    def split_pairs(self, text: str) -> Iterable[str]:
        """
        Split the string into pairs of two characters.
        If the string contains an odd number of characters,
        then the missing second character of the final pair should be replaced with an underscore ('_').

        Input: A string.

        Output: A list or another Iterable of strings.
        """

        # if len(text) % 2 == 1:       # Mine (humanity)
        #     new_text = text + '_'
        # else:
        #     new_text = text
        # return [new_text[::2][index] + new_text[1::2][index] for index in range(len(new_text[::2]))]

        return [text[::2][index] + (text if len(text) % 2 == 0 else text + '_')[1::2][index]
                for index in range(len(text[::2]))]

    # Correct Sentence
    def correct_sentence(self, text: str) -> str:
        """
        For the input of your function, you will be given one sentence.
        You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

        Pay attention to the fact that not all of the fixes are necessary.
        If a sentence already ends with a period (dot), then adding another one will be a mistake.

        Input: A string (str).

        Output: A string (str).
        """

        # new_text = text     # Mine
        # if not text[0].isupper():
        #     new_text = new_text[0].upper() + new_text[1:]
        # if text[-1]!='.':
        #     new_text += '.'

        # return text[0].upper() + text[1:] + ('.' if not text.endswith('.') else '')   # chatGPT

        # Mine is advanced
        return (text[0].upper() + text[1:] if not text[0].isupper() else text) + ('.' if text[-1] != '.' else '')

    # Nearest Value
    def nearest_value(self, values: set[int], one: int) -> int:
        """
        Find the nearest value to the given one.

        You are given a set of integers and a value for which you need to find the nearest one.

        For example, we have the following sequence of numbers: 4, 7, 10, 11, 12, 17,
        and we need to find the nearest value to the number 9. If we sort this sequence in the ascending order,
        then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7,
        which means that the correct answer is 10.

        A few clarifications:

        If 2 numbers are at the same distance, you need to choose the smallest one;
        The sequence of numbers is always non-empty;
        The given value can be in this sequence, which means that it’s the answer;
        The sequence may contain both positive and negative numbers, but they are always integers;
        The sequence isn’t sorted and consists only unique numbers.

        Input: Two arguments. A set of integers. The sought value as an integer.

        Output: An integer.

        """
        if one in values:
            return one

        for value in values:
            ...


if __name__ == '__main__':
    pyCheckiO_lessons = PyCheckiOLessons()
    result = pyCheckiO_lessons.nearest_value({17, 4, 7, 10, 11, 12}, 9)  # ...
    print(result)
