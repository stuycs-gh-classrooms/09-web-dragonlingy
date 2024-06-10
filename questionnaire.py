#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

import random

f = open("data/questions.txt", encoding = "utf-8")
questions = f.read()
f.close()

genderq = questions.split("Question: ")[1]
questions = questions.split("Prefer not to answer")[1:][0]

#print(genderq)
#print(questions)
f2 = open("data/characters.txt", encoding = "utf-8")
charactersmbti = f2.read()
f2.close()

charactersmbti = charactersmbti.split("*CHARACTERS*\n~Male")[1]
#print(charactersmbti)
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

def colorpicker(mbtir):
    color = ['', '']
    if(mbtir == "INTJ"):
        color[0] = '#d9d2e9'
        color[1] = '#000000'
    elif(mbtir == "INTP"):
        color[0] = '#b4a7d6'
        color[1] = '#000000'
    elif(mbtir == "ENTJ"):
        color[0] = '#8e7cc3'
        color[1] = '#ffffff'
    elif(mbtir == "ENTP"):
        color[0] = '#674ea7'
        color[1] = '#ffffff'
    elif(mbtir == "INFJ"):
        color[0] = '#d9ead3'
        color[1] = '#000000'
    elif(mbtir == "INFP"):
        color[0] = '#b6d7a8'
        color[1] = '#000000'
    elif(mbtir == "ENFJ"):
        color[0] = '#93c47d'
        color[1] = '#ffffff'
    elif(mbtir == "ENFP"):
        color[0] = '#6aa84f'
        color[1] = '#ffffff'
    elif(mbtir == "ISTJ"):
        color[0] = '#c9daf8'
        color[1] = '#000000'
    elif(mbtir == "ISFJ"):
        color[0] = '#a4c2f4'
        color[1] = '#000000'
    elif(mbtir == "ESTJ"):
        color[0] = '#6d9eeb'
        color[1] = '#ffffff'
    elif(mbtir == "ESFJ"):
        color[0] = '#3c78d8'
        color[1] = '#ffffff'
    elif(mbtir == "ISTP"):
        color[0] = '#fff2cc'
        color[1] = '#000000'
    elif(mbtir == "ISFP"):
        color[0] = '#ffe599'
        color[1] = '#000000'
    elif(mbtir == "ESTP"):
        color[0] = '#ffd966'
        color[1] = '#000000'
    else:
        color[0] = '#f1c232'
        color[1] = '#000000'
    return color
ext_int = 10
sen_ntu = 10
thi_fee = 10
jud_per = 10
def splitionary(text, delimiter, ending):
    split = {}
    g = text.split(delimiter)
    split[g[0]] = g[1:ending]
    return split

def all_questions(qs):
    split_qs = []
    g = qs.split("Question: ")[1:]
    for x in g:
        split_qs.append(splitionary(x, "\n", 5))
    return split_qs

def isolate_option(string, index):
    g = string.split(": ")
    return g[index]

characters = charactersmbti.split("*MBTI*")[0]
mbtis = charactersmbti.split("*MBTI*")[1]

male = characters.split("~Female")[0]
male = male.split("\n")[1:]
female = characters.split("~Female")[1]
female = female.split("\n")[1:]

def makeprofile(listinfo):
    info = []
    info.append(listinfo[0])
    info.append(listinfo[1])
    info.append(listinfo[2])
    bio = listinfo[3] + listinfo[4]
    info.append(bio)
   # info.append(listinfo[5])
    return info
dm = []
for l in male:
    dm.append(splitionary(l, "+", 6))
df = []
for l in female:
    df.append(splitionary(l, "+", 6))

#print(female)
#print(colorpicker("ISTJ"))
#print(all_questions(questions)[0])
data = cgi.FieldStorage()
#data = [1]
#check if any form data present
if (len(data) != 0):
    name = 'batman'
    if ('name' in data):
        name = data['name'].value
    gender = 'Other'
    if('gender' in data):
        gender = data['gender'].value
    bgcolor = '#000000'
    i = 1
    while(i <= 20):
        temp = "q" + str(i)
        if(temp in data):
            response = data[temp].value
        tempq = all_questions(questions)[i-1]
        tempq_onlyq = list(tempq.keys())[0]
        valueq = isolate_option(tempq_onlyq, 1)
        extent = 0
        for j in list(tempq.values())[0]:
            if(response in j):
                extent = int(isolate_option(j, 2))
        if(valueq == "ext_int"):
            ext_int += extent
        elif(valueq == "sen_ntu"):
            sen_ntu += extent
        elif(valueq == "thi_fee"):
            thi_fee += extent
        else:
            jud_per += extent
        i += 1
    mbti = ''
    if(ext_int == 10):
        if(random.randrange(2) == 0):
            mbti += 'E'
        else:
            mbti += 'I'
    elif(ext_int > 10):
        mbti += 'E'
    else:
        mbti += 'I'
    if(sen_ntu == 10):
        if(random.randrange(2) == 0):
            mbti += 'S'
        else:
            mbti += 'N'
    elif(sen_ntu > 10):
        mbti += 'S'
    else:
        mbti += 'N'
    if(thi_fee == 10):
        if(random.randrange(2) == 0):
            mbti += 'T'
        else:
            mbti += 'F'
    elif(thi_fee > 10):
        mbti += 'T'
    else:
        mbti += 'F'
    if(jud_per == 10):
        if(random.randrange(2) == 0):
            mbti += 'J'
        else:
            mbti += 'P'
    elif(jud_per > 10):
        mbti += 'J'
    else:
        mbti += 'P'
    if(gender == 'Male'):
        for j in dm:
            tempchr = list(j.keys())[0]
            templist = []
            finbio = []
            if(j[tempchr][0] == mbti and j[tempchr] != []):
                templist += list(tempchr)
                templist += j[tempchr][1:]
                finbio = makeprofile(templist)
    elif(gender == 'Female'):
        for j in df:
            tempchr = list(j.keys())[0]
            templist = []
            finbio = []
            if(j[tempchr][0] == mbti and j[tempchr] != []):
                templist += list(tempchr)
                templist += j[tempchr][1:]
                finbio = makeprofile(templist)
    else:
        if(random.randrange(2) == 0):
            for j in dm:
                tempchr = list(j.keys())[0]
                templist = []
                finbio = []
                if(j[tempchr][0] == mbti and j[tempchr] != []):
                    templist += list(tempchr)
                    templist += j[tempchr][1:]
                    finbio = makeprofile(templist)
        else:
            for j in df:
                tempchr = list(j.keys())[0]
                templist = []
                finbio = []
                if(j[tempchr][0] == mbti and j[tempchr] != []):
                    templist += list(tempchr)
                    templist += j[tempchr][1:]
                    finbio = makeprofile(templist)
    colors = colorpicker(mbti)
    bgcolor = colors[0]
    tcolor = colors[1]
    body = '<body style="color: '
    body += tcolor + ';">'
    body = '<body style="background-color: '
    body += bgcolor + ';">'
    body += '<h1>Congratulations, ' + name + '! Your MBTI is ' + mbti + '.</h1>'
    body += '<h2> Your corresponding character is... </h2> <h3>' + finbio[0] + '</h3>'
    body += '<h4>' + finbio[1] + '</h4>'
    body += '<p> <img src="' + finbio[2] + '" height = 200 width = 200>'
    body += finbio[3]
    body += '<br> Learn more about this character here: '
    for i in finbio[4].split(' '):
        body += i
        body += '<br>'
    body += 'Do you like this character?</p>'
    body += '<br><a href="questionnaire.py">Try Again</a>'
    html = make_html('Form Result', body)
    print(html)
#if no form data, return the form html instead of result
else:
    body = '<h1>Personality Test</h1>'
    body += '<p> DISCLAIMER: All questions are purely hypothetical and have no relation to any events that may occur in real life. These questions were written by Sarah Zou & Naomi Hsieh, and based off of the questions found <a href = "https://ays-pro.com/blog/16-personality-test-50-questions-and-answers.">here</a>. </p> <br>' 
    body += make_nameoption() + '<br>'
    tgq = splitionary(genderq, "\n", 5)
    gisolated = []
    for j in list(tgq.values())[0]:
        gisolated.append(isolate_option(j, 1))
    tgq_onlyq = list(tgq.keys())[0]
    gisolatedq = isolate_option(tgq_onlyq, 0)
    body += make_question(gisolatedq, "gender", gisolated) + '<br>'
    i = 0
    while(i < 20):
        tempq = all_questions(questions)[i]
        isolated = []
        for j in list(tempq.values())[0]:
            isolated.append(isolate_option(j, 1))
        tempq_onlyq = list(tempq.keys())[0]
        isolatedq = isolate_option(tempq_onlyq, 0)
        body += make_question(isolatedq, i+1, isolated) + '<br>'
        i += 1
    body+= '<input type="submit" value="Submit!">'
    html = make_html('Results!', body)
    print(html)
