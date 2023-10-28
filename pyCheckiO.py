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


if __name__ == '__main__':
    pyCheckiO_lessons = PyCheckiOLessons()
    result = pyCheckiO_lessons.is_even(num=110)
    print(result)
