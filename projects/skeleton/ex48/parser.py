# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:42:48 2016

@author: Administrator
"""

class ParserError(Exception):
    pass

class Sentence(object):
    
    def __init__(self, subject, verb, object, amount, times):
        #  remember  we  take  ('noun','princess')  tuples  and  convert  them
        self.subject=subject[1]
        self.verb=verb[1]
        self.object=object[1]
        self.amount=None
        self.times=None
        if amount!=None:
            self.amount=amount[1]
        if times!=None:
            self.times=times[1]
        
def peek(word_list):
    if word_list:
        word=word_list[0]
        return word[0]
    else:
        return None
        
def match(word_list, expecting):
    if word_list:
        word=word_list.pop(0)
        if word[0]==expecting:
            return word
        else:
            return None
    else:
        return None
        
def skip(word_list, word_type):
    typeplus=(word_type, 'error')
    while peek(word_list) in typeplus:
        match(word_list, word_type)
        
def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")
        
def parse_object(word_list):
    skip(word_list, 'stop')
    next=peek(word_list)
    
    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")
        
def parse_number(word_list):
    skip(word_list, 'stop')
    next=peek(word_list)
    
    if next == 'number':
        return match(word_list, 'number')
        
def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    amount=parse_number(word_list)
    obj=parse_object(word_list)
    times=parse_number(word_list)
    
    return Sentence(subj, verb, obj, amount, times)
    
def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)
    
    if start=='noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        #  assume  the  subject  is  the  player  then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object or verb not: %s" % start)
