"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None



def binary_search(a: List, x):
    l = 0
    r = len(a)-1
    while l <= r:
        m = ((l+r)//2)
        if x == a[m]:
            return m
        # search for x in first half
        if x < a[m]:
            r = m -1
        # search for x in second half
        elif x > a[m]:
            l = m + 1
    return None

def _merge(a0: List, a1: List, a: List):
    i_0 = 0
    i_1 = 0
    for i in range(len(a)):
        if i_0 == len(a0):
            a[i] = a1[i_1]
            i_1 += 1
        elif i_1 == len(a1):
            a[i] = a0[i_0]
            i_0 += 1
        elif a0[i_0] <= a1[i_1]:
            a[i] = a0[i_0]
            i_0 += 1
        else:
            a[i] = a1[i_1]
            i_1 += 1

def merge_sort(a: List):
    if len(a) == 1 or len(a) == 0:
        return a
    m = (len(a)//2)
    #let a0 be the first half of the array
    a0 = a[0:m]
    #let a1 be the second half of the array
    a1 = a[m:len(a)]
    merge_sort(a0)
    merge_sort(a1)
    # merge a0 and a1
    _merge(a0, a1, a)

def _partition_(a: List, start, end):
    piv = a[start]
    l = start + 1
    r = end
    while l <= end and a[l] <= piv:
        l += 1
    while r >= start and a[r] > piv:
        r -= 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        while a[l] <= piv and l <= end:
            l += 1
        while a[r] > piv and r >= start:
            r -= 1
    a[start], a[r] = a[r], a[start]
    return r

def _quick_sort_f(a: List, start, end):
    #first element for the sorting
    if start < end:
        i_p = _partition_(a, start, end)
        _quick_sort_f(a, start, i_p - 1)
        _quick_sort_f(a, i_p + 1, end)

def _partitiones_(a: List, start, end):
    rando = random.randint(start, end)
    a[start], a[rando] = a[rando], a[start]
    piv = a[start]
    l = start + 1
    r = end
    while l <= end and a[l] <= piv:
        l += 1
    while r >= start and a[r] > piv:
        r -= 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        while a[l] <= piv and l <= end:
            l += 1
        while a[r] > piv and r >= start:
            r -= 1
    a[start], a[r] = a[r], a[start]
    return r

def _quick_sort_r(a: List, start, end):
    #random element for quick sorting as the pivot
    if start < end:
        i_p = _partitiones_(a, start, end)
        _quick_sort_r(a, start, i_p - 1)
        _quick_sort_r(a, i_p + 1, end)



def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
