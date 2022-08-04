
import random as rand   #To generate random numbers
import numpy as np      #To calculate the product of complex numbers
import print_Question_Options as display    #To display the question,options and ansers
import generate_Latex_Format as latex      #To format the output in latex format
import JSON_Formatters
import json
'''
Author      : Bhathrinaathan M B
Description : Generates a complex number multiplication question with given number of options 
Last Updated on : 3rd August 2022
'''

author_Name='Bhathrinaathan M B'
guid_Id='08d3ea48-d909-4d98-8c45-81d6abaceb1b'
sys_Id='Hexint09'
reveiwer_Name='Sudharshana Venkatesh'
reveiwer_Id=''


#Genrates a complex number using randint function
def generate_complex_number(complexity):
    boundary={1:(1,10),2:(11,25),3:(20,30),4:(25,40),5:(30,40)}
    real=rand.randint(boundary[complexity][0],boundary[complexity][1])
    imag=rand.randint(boundary[complexity][0],boundary[complexity][1])
    operation=rand.randint(1,4)
    operator='+' if operation<3 else '-'
    return complex(str(real)+operator+str(imag)+'j')


#Genrates a question with demanded number of options
def generate_question(complexity,number_of_options):
    options=[]
    number_of_terms=2 if complexity<=3 else 3   #Decides the number of terms to be created
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
    ques_latex,options_latex,answer_latex=latex.format_question_complex_number(terms,options[:number_of_options],answer,'*')
    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer_latex,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    json.dumps(data)
    print(data)
    print('-'*120)


if __name__=='__main__':
    number_of_question=int(input("Enter the number of questions required : "))
    for i in range(0,number_of_question):
        complexity=int(input("Enter the complexity (1-5) : "))
        number_of_options=int(input("Number of options required : "))
        complexity=complexity if complexity>0 and complexity<6 else 3
        generate_question(complexity,number_of_options)
