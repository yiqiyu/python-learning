# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:14:35 2016

@author: Administrator
"""

from nose.tools import *
from nose.tools import assert_raises
from ex48 import lexicon
from ex48 import parser


def test_peek():
    assert_equal(parser.peek(lexicon.scan("north")), 'direction')
    assert_equal(parser.peek(lexicon.scan("go")), 'verb')
    assert_equal(parser.peek(lexicon.scan("the")), 'stop')
    assert_equal(parser.peek(lexicon.scan("bear")), 'noun')
    assert_equal(parser.peek(lexicon.scan("55")), 'number')
    assert_equal(parser.peek(lexicon.scan("erheh")), 'error')
   
def test_match():
    wordlist={'direction':"east", 'verb':"eat", 'stop':"in", 'noun':"princess", 'number':324, 'error':"err"}
    for (wtype,word) in wordlist.items():
        result=lexicon.scan(word)
        assert_equal(parser.match(result,wtype)[1], word)
        assert_equal(parser.match(result,wtype), None)
    result=lexicon.scan("kill")
    assert_equal(parser.match(result, 'noun'), None)
                          
def test_parsesverb():
    testsentence="the princess eat the bear"
    result=lexicon.scan(testsentence)
    assert_raises(parser.ParserError, parser.parse_verb, result)
    testsentence="eat the bear"
    result=lexicon.scan(testsentence)
    assert_equal(parser.parse_verb(result), ('verb','eat'))
                       
def test_parsesobject():
    testsentence="the kill princess eat the bear"
    result=lexicon.scan(testsentence)
    assert_raises(parser.ParserError, parser.parse_object, result)
    testsentence="the princess eat the bear"
    result=lexicon.scan(testsentence)
    assert_equal(parser.parse_object(result), ('noun','princess'))
    testsentence="north"
    result=lexicon.scan(testsentence)
    assert_equal(parser.parse_object(result), ('direction','north'))
    
def test_parse_number():
    testsentence="100 bear"
    result=lexicon.scan(testsentence)
    assert_equal(parser.parse_number(result), ('number', 100))
    testsentence="kill bear"
    result=lexicon.scan(testsentence)
    assert_equal(parser.parse_number(result), None)
    
def test_parsessubject():
    testsentence="eat the bear"
    result=lexicon.scan(testsentence)
    sentence=parser.parse_subject(result,('noun','player'))
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'bear')
                          
def test_sentence():
    testsentence="the princess eat 100 bear 14 times"
    result=lexicon.scan(testsentence)
    sentence=parser.parse_sentence(result)
    assert_equal(sentence.subject, 'princess')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.amount, 100)
    assert_equal(sentence.object, 'bear')
    assert_equal(sentence.times, 14)
    
    testsentence="eat the bear"
    result=lexicon.scan(testsentence)
    sentence=parser.parse_sentence(result)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'bear')
    
    testsentence="sdfsdfsf princess eat the bear"
    result=lexicon.scan(testsentence)
    sentence=parser.parse_sentence(result)
    assert_equal(sentence.subject, 'princess') 
