# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 16:03:44 2016

@author: Yiqi Yu

一个计算格罗夫斯克拉克维特瑞机制的小程序，输入一个每个个体对于两个选择的价值表，计算出
最后集体应该选的选择并且计算出为此每个人应该付的税金

《博弈与社会》P666
"""
class VCG(object):
    def __init__(self, form):
        self.domain=form
        self.row=len(form)
        self.column=len(form[0])
        self._sum=[]
        for x in range(self.column):
            self._sum.append(0)
            for y in range(self.row):
                self._sum[x]=self._sum[x]+self.domain[y][x]
        
    def total_sum(self,col):
        return self._sum[col]
        
    def relate_sum(self,row,col):
        return self._sum[col]-self.domain[row][col]

    def decision(self):
       if self._sum[0]>self._sum[1]:
           return 0
       else:
           return 1
           
    def determine(self,x):
        if (self.relate_sum(x,0)-self.relate_sum(x,1))*\
        (self._sum[0]-self._sum[1])<0:
            return True
        else:
            return False
    
    def tax(self):
        payment=[]
        for x in range(self.row):
            if self.determine(x):
                a=(x,abs(self.relate_sum(x,0)-self.relate_sum(x,1)))
                payment.append(a)
        for i in payment:
            print "%d pays %d" % (i[0],i[1])
        return
        
    def get_decision(self):
        print "We decided to pick choice no.%d " % (self.decision()+1)
        return
        

def calculate_input():
    form=[[10,30],[30,10],[15,20],[25,10]]
    new=VCG(form)
    new.get_decision()
    new.tax()
    
if __name__=='__main__':
    calculate_input()


        
        
        
    
    
    