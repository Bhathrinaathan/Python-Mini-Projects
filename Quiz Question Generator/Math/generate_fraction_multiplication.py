import random as rand 
from fractions import Fraction as frac
import numpy
import print_Question_Options as display

def generate_number(complexity):
    bound={1:(1,5), 2:(5,25), 3:(10,50), 4:(15,100), 5:(20,200)}
    return (rand.randint(bound[complexity][0],bound[complexity][1]))

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
    display.print_Ques_Opt_Ans(terms,options,number_of_options,product)

if __name__=='__main__':
    generate_question(4,4)
