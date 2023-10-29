class PyCheckiOLessons():

    def __init__(self, ):
        ...

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

        # integer_text = 0
        # 
        # for string in text:
        #     if string.isdigit():
        #         integer_text += int(string)

        return sum(int(string) for string in text.split(' ') if string.isdigit())


if __name__ == '__main__':
    pyCheckiO_lessons = PyCheckiOLessons()
    result = pyCheckiO_lessons.sum_numbers("23 my 23 numbers 1st is ")
    print(result)
