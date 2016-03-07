# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:38:51 2016

@author: Administrator
"""

import web

urls=(
    '/hello', 'Index'
)

app=web.application(urls, globals())

render  =  web.template.render('C:\\Users\\Administrator\\Desktop\\python\\projects\\gothonweb\\templates\\',  base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()
    
    def POST(self):
        form = web.input(name="Nobody",  greet="Hello")
        greeting = "%s,  %s"  %  (form.greet,  form.name)
        return render.index(greeting  =  greeting)

        
if __name__=="__main__":
    app.run()