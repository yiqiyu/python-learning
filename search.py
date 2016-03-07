# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:20:23 2016

@author: Administrator

当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
并打印出完整路径

"""

import os
import os.path

#函数里层，负责搜索
def innersearch(s, spath, store):
    slist=os.listdir(spath)
    for x in slist:
        full_path=spath+'\\'+x      #给每个文件和文件夹补全路径
        if os.path.isfile(full_path) and s in x:   
            print full_path
            store.append(full_path)   #符合条件的文件将被打印并存入store中
        elif os.path.isdir(full_path):
            innersearch(s, full_path, store)    #文件夹将继续搜索

#函数外层，若没有搜索到指定文件将打印信息
def search(s, spath='.'):
    store=[]    #搜索到的文件数据会记录在里面
    innersearch(s, spath, store)
    if len(store)==0:
        print 'Not found!'

#测试效果，以ex48和vv为例
if __name__=='__main__':
    search('ex48','C:\Users\Administrator\Desktop\python')  
    print '--------------'
    search('vv','C:\Users\Administrator\Desktop\python')

        