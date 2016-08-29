# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 12:16:40 2016

@author: Administrator
"""

def SimpleSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]


def BubbleSort(array):
    hasSwitched = True
    for i in range(len(array)):
        hasSwitched = False
        for j in range(1, len(array)-i):
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


def HeapSort(array):
    l = len(array)
    for i in range(1, l/2+1):
        _heapAdjust(array, l/2-i, l)
    for i in range(1, l-1):
        array[l-i], array[0] = array[0], array[l-i]
        _heapAdjust(array, 0, l-i-1)


def _heapAdjust(array, currentRoot, currentRegion):
    t = array[currentRoot]
    child = (currentRoot+1)*2-1
    while child < currentRegion:
        #找孩子中较大的一个
        if child < currentRegion-1:
            if array[child] < array[child+1]:
                child += 1
        #如果根已经比孩子们都大，跳过
        if t >= array[child]:
            break
        array[currentRoot] = array[child]
        #将更改过的子树作为下一循环的处理对象
        currentRoot = child
        child *= 2
    array[currentRoot] = t
    
def MergeSort(array):
    p = []
    _mergeSort(array, 0, len(array)-1, p)
    

def _mergeSort(array, low, high, temp):
    if low < high:
        mid = (low+high)/2
        _mergeSort(array, low, mid, temp)
        _mergeSort(array, mid, high, temp)
        _merge(array, low, mid, high)
        

def _merge(array, low, mid, high, sortedArray):
    i = low
    j = mid+1
    m = high
    n = mid
    k = 0
    while i < n and j < m:
        if array[i] < array[j]:
            sortedArray[k] = array[j]
            k += 1
            j += 1
        else:
            sortedArray[k] = array[i]
            k += 1
            j += 1
    #比较剩下的直接插后面
    if i < n:
        sortedArray[k:] = array[i:n]
    if j < m:
        sortedArray[k:] = array[j:m]    


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


s=[4,3,1,6]
HeapSort(s)
print s