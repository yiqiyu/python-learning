# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:25:57 2015

@author: Administrator
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config={
    "description":"My Project",
    "author":'My Name',
    'url':'URL to get it at',
    'download_url':'Where to download it.',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['ex48'],
    'scripts':[],
    'name':'projects'
}

setup(**config)