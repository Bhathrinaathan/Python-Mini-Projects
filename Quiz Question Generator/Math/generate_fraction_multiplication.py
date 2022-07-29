import random as rand   #To generate random numbers
from fractions import Fraction as frac  #To use the fractions 
import numpy    #To calculate the product of complex numbers
import print_Question_Options as display    #Display the questions , options and answer
import generate_Latex_Format as latex      #To format the output in latex format
import JSON_Formatters
import json

author_Name='Bhathrinaathan M B'
guid_Id='6daace42-bb63-4c2a-8785-038821f1be1a'
sys_Id='Hexint09'
reveiwer_Name=''
reveiwer_Id=''
#Genrates a random number for the given complexity
def generate_number(complexity):
    bound={1:(1,5), 2:(5,25), 3:(10,50), 4:(15,100), 5:(20,200)}
    return (rand.randint(bound[complexity][0],bound[complexity][1]))

#Genrates a complex number using randint function
def generate_fraction(complexity):
    return (frac(generate_number(complexity),generate_number(complexity)))

def generate_question(complexity,number_of_options):
    number_of_terms=2 if complexity<=2 else 3
    terms=[generate_fraction(complexity) for i in range(0,number_of_terms)]
    product=numpy.prod(terms)
    numerator_start=product.numerator-number_of_options if product.numerator-number_of_options else product.numerator

    options=[frac(i,product.denominator) for i in range(numerator_start,numerator_start+number_of_options+1)] 
    rand.shuffle(options)

    if product not in options[:-1:]:
        options[number_of_options-1]=product
    display.print_Ques_Opt_Ans(terms,options,number_of_options,product,'*')
    ques_latex,options_latex,answer_latex=latex.format_question_fraction_number(terms,options[:number_of_options],product,'*')
    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer_latex,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    json.dumps(data)


if __name__=='__main__':
    generate_question(4,4)
