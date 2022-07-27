'''
Author : Bhathrinaathan M B
'''
def operation_question(operator):
    spc='\:'
    if operator=='+':
        operation='addition'
    elif operator=='-':
        operation='subtraction'
    elif operator =='*':
        operation='multiplication'
    else:
        operation='division'
    return "Solve"+spc+operation+spc+"for"+spc+"the"+spc+"following"+spc+":\:\:"

def format_question_complex_number(terms,options,answer,operator):
    question=operation_question(operator)
    spc='\:'
    for i in terms[::-2]:
        question+=(spc+str(i)+spc+operator)
    question+=str(terms[-1])
    opts=list(map(lambda a : str(a),options))
    return (question,opts,str(answer))

def format_question_fraction_number(terms,options,answer,operator):
    question=operation_question(operator)
    spc='\:'
    for i in terms[::-2]:
        question+=(spc+" \\frac{"+str(i.numerator)+"}{"+str(i.denominator)+'}'+spc+operator+spc)
    question+=(spc+" \\frac{"+str(i.numerator)+"}{"+str(i.denominator)+'}'+spc+":")
    opt=list(map(lambda a: "\\frac{"+str(a.numerator)+"}{"+str(a.denominator)+'}'+spc,options))
    answer=(" \\ frac{"+str(answer.numerator)+"}{"+str(answer.denominator)+"}")
    return (question,opt,answer)
