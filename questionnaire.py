#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

f = open("data/questions.txt", encoding = "utf-8")
questions = f.read()
f.close()

f2 = open("data/characters.txt", encoding = "utf-8")
characters = f2.read()
f2.close()

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

def make_question(question, number, options):
    html = ""
    form = question + "\n"
    
    for option in options:
        inputo = '<div>'
        inputo+= '<input type="radio" name="q' + str(number) + '" value="' + option + '">'
        inputo+= option + '</div>'
        form += inputo
    
    html+= form
    return html


ext_int = 10
sen_ntu = 10
thi_fee = 10
jud_per = 10
def split_question(question):
    split = {}
    g = question.split("\n")
    split[g[0]] = g[1:5]
    return split

def all_questions(qs):
    split_qs = []
    g = qs.split("Question: ")[1:]
    for i in g:
        split_qs.append(split_question(i))
    return split_qs

def isolate_option(string):
    g = string.split(": ")
    return g[1]

#print(all_questions(questions)[0])
data = cgi.FieldStorage()
#check if any form data present
if (len(data) != 0):
    name = 'batman'
    if ('name' in data):
        name = data['name'].value
    bgcolor = 'DarkSeaGreen'
    if ('bgcolor' in data):
        bgcolor = data['bgcolor'].value
    i = 1
    responses = {}
    while(i <= 20):
        temp = "q" + str(i)
        if(temp in data):
            responses[temp] = data[temp].value
        i += 1
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
    i = 0
    while(i < 20):
        tempq = all_questions(questions)[i]
        isolated = []
        for j in list(tempq.values())[0]:
            isolated.append(isolate_option(j))
        body+= make_question(list(tempq.keys())[0], i+1, isolated)
        i += 1
    body+= '<input type="submit" value="Submit!">'
    html = make_html('Form Results', body)
    print(html)
