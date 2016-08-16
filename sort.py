# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:16:40 2016

@author: Administrator
"""

def SimpleSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]


def BubbleSort(array):
    hasSwitched = True
    for i in range(len(array)):
        hasSwitched = False
        for j in range(1,len(array)-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                hasSwitched = True
        if not hasSwitched: break

def InsertSort(array):
    for i in range(1,len(array)):
        j = i
        while j >= 1 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


def QuickSort(array):
    _quickSort(array, 0, len(array))


def _quickSort(array, low, high):
    if low <= high:
        i = low
        j = high
        x = array[i]
        while i < j:
            while i < j and array[j] >= x:
                j -= 1
            if i < j:
                array[i] = array[j]
                i += 1
            while i < j and array[i] <= x:
                i += 1
            if i < j:
                array[j]= array[i]
                j -= 1
        array[i] = x
        _quickSort(array, low, i-1)
        _quickSort(array, i+1, high)


