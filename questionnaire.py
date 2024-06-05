#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

def make_html(title, body):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="utf-8">
    """
    html+= '<title>' + title + '</title></head>'
    html+= '<body>' + body + '</body>'
    html+= '</body></html>'
    return html

def make_nameoption():
    html = """
    <form action="questionnaire.py" method="GET">"""
    html += "Name: "
    html += """ <input type="text" name="name" value="Bob">
    <br>
    """
    return html

def make_form(question, options):
    html = ""
    form = question + "\n"
    
    for option in options:
        inputo = '<div>'
        inputo+= '<input type="radio" name="bgcolor" value="' + option + '">'
        inputo+= option + '</div>'
        form += inputo
    
    html+= form
    html+= '<input type="submit" value="Submit!">'
    return html



data = cgi.FieldStorage()
#check if any form data present
if (len(data) != 0):
    name = 'batman'
    if ('name' in data):
        name = data['name'].value
    bgcolor = 'DarkSeaGreen'
    if ('bgcolor' in data):
        bgcolor = data['bgcolor'].value
    body = '<body style="background-color: '
    body+= bgcolor + ';">'
    body+= '<h1>Hello ' + name + '</h1>'
    body+= '<br><a href="questionnaire.py">Try Again</a>'
    html = make_html('Form Result', body)
    print(html)
#if no form data, return the form html instead of result
else:
    body = '<h1>Form Test</h1>'
    body+= make_nameoption()
    body+= make_form("What color are you?", ['LightPink', 'LightSkyBlue'])
    html = make_html('Form Results', body)
    print(html)
