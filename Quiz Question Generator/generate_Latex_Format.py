'''
Author      : Bhathrinaathan M B
Description : Formats questions,options and answers for various question types
Last updated on : 3rd August 2022
'''

spc='\:'
def operation_question(operator):
    if operator=='+':
        operation='addition'
    elif operator=='-':
        operation='subtraction'
    elif operator =='*':
        operation='multiplication'
    else:
        operation='division'
    return "Solve"+spc+operation+spc+"for"+spc+"the"+spc+"following"+spc+":\:\:"

#Complex Numbers
def format_question_complex_number(terms,options,answer,operator):
    question=operation_question(operator)
    for i in terms[::-2]:
        question+=(spc+str(i)+spc+operator)
    question+=str(terms[-1])
    opts=list(map(lambda a : str(a),options))
    return (question,opts,str(answer))

#Fraction Numbers
def format_question_fraction_number(terms,options,answer,operator):
    question=operation_question(operator)
    for i in terms[::-2]:
        question+=(spc+" \\frac{"+str(i.numerator)+"}{"+str(i.denominator)+'}'+spc+operator+spc)
    question+=(spc+" \\frac{"+str(i.numerator)+"}{"+str(i.denominator)+'}'+spc+":")
    opt=list(map(lambda a: "\\frac{"+str(a.numerator)+"}{"+str(a.denominator)+'}'+spc,options))
    answer=(" \\ frac{"+str(answer.numerator)+"}{"+str(answer.denominator)+"}")
    return (question,opt,answer)

#-------------------------------Coordinate Geometry---------------------#

#Distance between two points
def format_distace_btw_points(pt1,pt2,options,distance):
    question="Find"+spc+"the"+spc+"distance"+spc+"between"+spc+str(pt1)+spc+"and"+spc+str(pt2)+":\\"
    options=[str(i) for i in options]
    return question,options,str(distance)

#Section Formula
def format_section_formula(pt1,pt2,options,res_pt,m,n):
    if m is n:
        question="Find"+spc+"the"+spc+"point"+spc+"which"+spc+"bisects"+spc+"the"+spc+"line"+spc+"formed"+spc+"by"+spc+"the"+spc+"points"+spc+str(pt1)+spc+"and"+spc+str(pt2)+":"
    else:    
        question="Find"+spc+"the"+spc+"point"+spc+"which"+spc+"divides"+spc+"the"+spc+"line"+spc+"in"+spc+"the"+spc+"ratio"+spc+str(m)+"and"+spc+str(n)
    options=[str(i) for i in options]
    return question,options,str(res_pt)

#Area of Triangle

def format_area_of_triangle(A,B,C,options,area):
    question="Find"+spc+"the"+spc+"area"+spc+"of"+spc+"the"+spc+"triangle"+spc+"formed"+spc+"by"+spc+"points"+spc+str(A)+spc+","+str(B)+spc+"and"+spc+str(C)+":"
    options=[str(i) for i in options]
    return question,options,str(area)

#Collinearity

def format_collinearity(A,B,C):
    ques="Is"+spc+'the'+spc+'points'+str(A)+','+spc+str(B)+'and'+spc+str(C)+'follows'+spc+'collinearity:'
    return ques

#------------------------------------Name It---------------------------------------------#

def format_string_latex(string):
    latex_str=''
    for i in list(string.split()):
        latex_str+=str(i)+spc
    return latex_str


def format_name_it(question,options,answer):
    ques_latex=format_string_latex(question)
    options_latex=[format_string_latex(i) for i in options]
    answer_latex=format_string_latex(answer)
    return ques_latex,options_latex,answer_latex