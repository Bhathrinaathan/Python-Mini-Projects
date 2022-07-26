import random as rand   #To generate random numbers
import numpy as np      #To calculate the product of complex numbers
import print_Question_Options as display


#Calculates the number of terms to generate for the given complexity
def calculate_number_of_terms(complexity):
    if complexity<=3:
        return 2;
    return 3; 

#Genrates a complex number using randint function
def generate_complex_number(complexity):

    boundary={1:(1,10),2:(11,25),3:(20,30),4:(25,40),5:(30,40)}
    real=rand.randint(boundary[complexity][0],boundary[complexity][1])
    imag=rand.randint(boundary[complexity][0],boundary[complexity][1])
    operation=rand.randint(1,4)
    operator='+' if operation<=3 else '-'
    return complex(str(real)+operator+str(imag)+'j')

#Genrates a question with demanded number of options
def generate_question(complexity,number_of_options):
    options=[]
    number_of_terms=calculate_number_of_terms(complexity)
    terms=[generate_complex_number(complexity) for i in range(0,number_of_terms)]   #generates complex numbers
    answer=complex(np.prod(terms))  #Calculate the product using prof function of Numpy

    flag=int(number_of_options/2)
    for i in range((-1*flag),flag):     #Genrates suitable options and append it to the options list
        if (i!=0):
            options.append(i+answer)
            options.append(complex(str(i)+'j')+answer)
    rand.shuffle(options)
    options[rand.randint(0,number_of_options-1)]=answer
    display.print_Ques_Opt_Ans(terms,options,number_of_options,answer,'*')


if __name__=='__main__':
    generate_question(3,4)
