# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:44:49 2016

@author: Administrator
"""

def scan(sentence):
 
    direction=['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verb=['go', 'stop', 'kill', 'eat']
    stop=['the', 'in', 'of', 'from', 'at', 'it']
    noun=['door', 'bear', 'princess', 'cabinet']
    keywords={'direction' : direction, 'verb' : verb, 'stop' : stop, 'noun' : noun}
    
    ResultList=[]
    FType=None
    
    if not isinstance(sentence, int):
        sentence=sentence.lower()
    else:
        sentence=str(sentence)
    words=sentence.split()
    for word in words:
        try:
            ResultList.append(('number', int(word))) 
        except ValueError:
            for (TypeName,WordType) in keywords.items():        #字典遍历方式http://www.jb51.net/article/50507.htm
                if word in WordType:
                    ResultList.append((TypeName, word))
                    FType=TypeName
            if FType==None:
                ResultList.append(('error', word))
        FType=None
    return ResultList
        
                
                