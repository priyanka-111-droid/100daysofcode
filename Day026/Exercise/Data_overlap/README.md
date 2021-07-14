# Data Overlap(Using list comprehension)

Instructions:

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4

result = [2, 3]

Hints:

1.First, you will need to read from the files and create a list using the lines in the files.

2.This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

3.Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

4.Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp