# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:46:35 2016

@author: Dante Yu

KMP模式匹配算法实现
"""

def nextval(string):
    MainI=1     #后缀序数
    SubI=0      #前缀序数
    l=len(string)   #串长
    nextlist=[0]    #next表，首位为0
    while MainI<l:
        if string[SubI]==string[MainI]:
            #字符相等则继续
            MainI+=1
            SubI+=1
            if string[SubI]!=string[MainI]:
                #当前字符与前缀不等时，前缀序数为nextlist值
                nextlist[MainI]=SubI
            else:
                #否则其nextlist值与前者相等
                nextlist[MainI]=nextlist[SubI]
        else:
            #否则回溯
            SubI=nextlist[SubI]
    return nextlist

def KMPMatch(MainStr, Target, Pos): 
#输入主串，目标和初始位置，如果存在目标串则返回第一次出现的位置，否则返回False
    nextlist=nextval(Target)
    ls=len(MainStr)   #主串的长度
    lt=len(Target)    #目标串的长度
    MainI=Pos
    SubI=0
    while MainI<ls and SubI<lt:
        #如果MainI和SubI均小于对应串长度时，循环继续
        if MainStr[MainI]==Target[SubI]: 
            #字符相等则继续
            SubI+=1
            MainI+=1
        else:
            SubI=nextlist[SubI]     #SubI否则按nextlist回溯
    if SubI>lt:     #判断目标串是否完整检索
        return MainI-lt
    else:
        return False
    
            