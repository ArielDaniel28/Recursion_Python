Recursion and Helper Functions

This Python module, `ex7_helper.py`, contains various recursive functions and helper functions for recursion.

## Table of Contents

- [Functions](#functions)
  - [mult](#mult)
  - [is_even](#is_even)
  - [log_mult](#log_mult)
  - [is_power](#is_power)
  - [reverse](#reverse)
  - [play_hanoi](#play_hanoi)
  - [number_of_ones](#number_of_ones)
  - [deep_compare](#deep_compare)
  - [compare_2d_lists](#compare_2d_lists)
  - [magic_list](#magic_list)

## Functions

### mult

- **Description:** This function calculates the multiplication of two numbers recursively and efficiently in O(n).

- **Parameters:**
  - `x` (float): The first number.
  - `y` (int): The second number.

- **Returns:**
  - `float`: The multiplication result of `x` and `y`.

### is_even

- **Description:** This function checks if a given integer is even using recursion.

- **Parameters:**
  - `n` (int): The integer to check.

- **Returns:**
  - `bool`: True if `n` is even, False otherwise.

### log_mult

- **Description:** This function calculates the multiplication of two numbers recursively and efficiently in O(log n).

- **Parameters:**
  - `x` (float): The first number.
  - `y` (int): The second number.

- **Returns:**
  - `float`: The multiplication result of `x` and `y`.

### is_power

- **Description:** This function checks if a given number is a power of another number using recursion.

- **Parameters:**
  - `b` (int): The base number.
  - `x` (int): The number to check if it's a power of `b`.

- **Returns:**
  - `bool`: True if `x` is a power of `b`, False otherwise.

### reverse

- **Description:** This function reverses a given string recursively.

- **Parameters:**
  - `s` (str): The string to reverse.

- **Returns:**
  - `str`: The reversed string.

### play_hanoi

- **Description:** This function solves the Tower of Hanoi problem recursively.

- **Parameters:**
  - `Hanoi` (Any): The Hanoi object or class.
  - `n` (int): The number of disks.
  - `src` (Any): The source tower.
  - `dst` (Any): The destination tower.
  - `temp` (Any): The temporary tower.

### number_of_ones

- **Description:** This function counts the number of occurrences of the digit '1' from 1 to a given number `n`.

- **Parameters:**
  - `n` (int): The number to count the occurrences of '1'.

- **Returns:**
  - `int`: The number of occurrences of '1'.

### deep_compare

- **Description:** This function recursively compares two 2D lists for equality.

- **Parameters:**
  - `list1`: The first 2D list.
  - `list2`: The second 2D list.
  - `column_index` (int): The current column index.
  - `value_index` (int): The current value index.

- **Returns:**
  - `bool`: True if the lists are equal, False otherwise.

### compare_2d_lists

- **Description:** This function compares two 2D lists for equality.

- **Parameters:**
  - `l1` (List[List[int]]): The first 2D list.
  - `l2` (List[List[int]]): The second 2D list.

- **Returns:**
  - `bool`: True if the lists are equal, False otherwise.

### magic_list

- **Description:** This function generates a nested list where each level represents the powers of 2.

- **Parameters:**
  - `n` (int): The depth of the nested list.

- **Returns:**
  - `List[Any]`: The nested list.

## License

This program was written by a student of the Introduction to Computer Science course at the Hebrew University in Jerusalem as part of the course requirements.
