#################################################################
# FILE : ex7.py
# WRITER : Ariel Daniel , arieldaniel28 , 208500710
# EXERCISE : intro2cs ex7 2022C
# STUDENTS I DISCUSSED THE EXERCISE WITH: Yarden Ashuah
# WEB PAGES I USED: None
#################################################################
from typing import Any, List
from ex7_helper import add, subtract_1, is_odd, divide_by_2, append_to_end

def mult(x: float, y: int) -> float:
    """Function that get the multiplication result of x and y in recursion way and in O(n) efficiency"""
    if y==1:
        return x
    return add(x, mult(x, subtract_1(y)))

def is_even (n: int) -> bool:
    """The function gets an variable 'n' and returns 'True' if even, 'False' if odd"""
    if n==0:
        return True
    if n==1:
        return False
    return is_even(subtract_1(subtract_1(n)))

def log_mult(x: float, y: int) -> float:
    """Function that get the multiplication result of x and y in recursion way and in O(log n) efficiency"""
    if y==1:
        return x
    z = log_mult(x, divide_by_2(y))
    if is_odd(y):
        return add(z,add(z,x))
    else:
        return add(z,z)

def is_power(b: int, x: int) -> bool:
    """Function that returns True if there is a number 'n' that b power n equals x, False if isn't"""
    if b==x or log_mult(b,b)==x:
        return True
    elif b>x:
        return False
    else:
        return is_power(b, divide_by_2(x))

def reverse(s: str) -> str:
    """Function that gets a string 's' and returns the same string but reversed"""
    if len(s)==1:
        return s
    return append_to_end(reverse(s[1:]),s[0])

def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any):
    if n<=0:
        pass
    elif n==1:
        Hanoi.move(src, dst)
    elif n==2:
        Hanoi.move(src,temp)
        Hanoi.move(src,dst)
        Hanoi.move(temp, dst)
    else:
        play_hanoi(Hanoi, n-1, src, temp, dst)
        Hanoi.move(src,dst)
        play_hanoi(Hanoi, n-1, temp, dst, src)

def number_of_ones(n: int) -> int:
    """Function that gets a number 'n' and return the number of times that digit '1' found in every number from 1 to n
    , include n itself"""
    if n==1:
        return 1
    elif n>0 and n<9:
        return 1
    elif n%10 == 1:
        return (1 + number_of_ones(n//10))
    else:
        return number_of_ones(n//10)

def deep_compare(list1, list2, column_index, value_index):
    """Function that gets two 2d lists, column index and value index and returns True if all of their coordinates are
     equal, otherwise returns False """
    if len(list1)!=len(list2):
        return False
    if len(list1)>column_index:
        if len(list1[column_index])!=len(list2[column_index]):
            return False
        if len(list1[column_index])>value_index:
            if list1[column_index][value_index]!=list2[column_index][value_index]:
                return False
            return deep_compare(list1,list2,column_index,value_index+1)
        return deep_compare(list1,list2,column_index+1,0)
    return True

def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """Function that gets two 2d lists and returns True if all of their coordinates are equal, otherwise returns False"""
    return deep_compare(l1,l2,0,0)

def magic_list(n: int) -> List[Any]:
    """Function that gets a number 'n' and returns a list in length 'n' that represents the number in the n'th place by
    this sequence:
    if n=0, return []
    if n=1, return [[]]
    if n=2 return [[],[[]]]
    and so on"""
    if n==0:
        return []
    new_list=magic_list(n-1)
    new_list.append(magic_list(n-1))
    return new_list

