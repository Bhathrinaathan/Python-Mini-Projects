import random as rand   #To generate random numbers
import math     #To calculate the square root
import print_Question_Options as display    #To display the question,options and ansers
import generate_Latex_Format as latex      #To format the output in latex format
import JSON_Formatters
import json
'''
Author      : Bhathrinaathan M B
Description : i)Generates a question for distance formula, to calculate distance between two points
              ii)Generates a question for bisection of line using section formula
              iii)Questions for a section of line divided with a ratio
              iv)Question to calculate a area of a triangle bounded by three points
              v)Question to check if three points are collinear or not
Last Updated on : 3rd August 2022
'''

author_Name='Bhathrinaathan M B'
guid_Id='08d3ea48-d909-4d98-8c45-81d6abaceb1b'
sys_Id='Hexint09'
reveiwer_Name='Sudharshana Venkatesh'
reveiwer_Id=''


#Generates the coordinates
def generate_coordinates(complexity):
    bound=complexity*5
    return (rand.randint(bound*-1,bound),rand.randint(bound*-1,bound))

#---------------------------------------------Distance Formula------------------------------------------------#

#Question about finding the distance between two points
def ques_Distance_btw_points(complexity,number_of_options):
   
    pt1=generate_coordinates(complexity)
    pt2=generate_coordinates(complexity)
    distance=round(math.sqrt( (pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2 ),2)   #Finds the answer
    options=[round(i+distance,2) for i in range(-1*number_of_options//2,number_of_options//2)]
    rand.shuffle(options)
    ques_latex,options_latex,answer_latex=latex.format_distace_btw_points(pt1,pt2,options,distance)

    display_ques=f"Find the distance between the points {pt1} and {pt2} :"
    display.print_questions_option_answer(display_ques,options,distance)

    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer_latex,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    data=json.dumps(data)
    return data

#-------------------------------------------------Area-------------------------------------------------------#

#Calculates the area of triangle
def triangle_and_area(complexity):                           #area(ABC)=|1/2{x1(y2-y3)+x2(y3–y1)+x3(y1–y2)}| 
    A=generate_coordinates(complexity)
    B=generate_coordinates(complexity)
    C=generate_coordinates(complexity)
    res_area=round(abs(0.5 * (A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]) )),2)
    return A,B,C,res_area

#Generates a question for finding the area of a triangle
def ques_area_of_triangle(complexity,number_of_options):
    A,B,C,area=triangle_and_area(complexity)
    options=[area+i for i in range(-1*number_of_options//2,number_of_options//2)]
    rand.shuffle(options)
    ques_latex,options_latex,answer_latex=latex.format_area_of_triangle(A,B,C,options,area)
    display_ques=f"Find the area of the triangle formed by points {A},{B} and {C} : "
    display.print_questions_option_answer(display_ques,options,area)
    
    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer_latex,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    json.dumps(data)
    return data

#Generates a question to find if a set of points is collinear
def ques_collinearity(complexity):              #Three point is said to be collinear if the area bounded by
    spc='\:'                                    #those points is 0
    A,B,C,area=triangle_and_area(complexity)
    options_latex=["True","False","Cannot"+spc+"be"+spc+"determined"]
    answer="True" if area==0 else "False"
    ques_latex=latex.format_collinearity(A,B,C)
    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    json.dumps(data)
    display.print_questions_option_answer(ques_latex,options_latex,answer)
    return data


#---------------------------------------------Section Formula------------------------------------------------#


#Section formula
def sectionFormula(pt1,pt2,m,n):
    x=(m*pt2[0]  + n*pt1[0])/(m+n)                          #x = (mx2+nx1) / (m+n)
    y=(m*pt2[1]  + n*pt2[0])/(m+n)                          #y = (my2+ny1) / (m+n)
    return (round(x,2),round(y,2))

#Common part for question generation
def section_of_line(complexity,number_of_options,m,n):
    pt1=generate_coordinates(complexity)
    pt2=generate_coordinates(complexity)
    res_pt=sectionFormula(pt1,pt2,m,n)
    options=[ (round(res_pt[0]+i,2),round(res_pt[1]+i,2)) for i in range(-1*number_of_options//2,number_of_options//2)]
    rand.shuffle(options)
    ques_latex,options_latex,answer_latex=latex.format_section_formula(pt1,pt2,options,res_pt,m,n)
    if m is n:  #For bisection type
        display_ques=f"Find the point which bisects the line between {pt1} and {pt2} :"
    else:       #Division with ratio
        display_ques=f"Find the point which divides line formed by the points {pt1} and {pt2} in ratio {m} and {n} "
    display.print_questions_option_answer(display_ques,options,res_pt)
    data=JSON_Formatters.format_json_file(ques_latex,options_latex,answer_latex,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    data=json.dumps(data)
    print(data)


#Finding a point bisecting a line between two points
def ques_bisection_of_line(complexity,number_of_options):
    return section_of_line(complexity,number_of_options,1,1)


#Finding a point dividing in a ratio
def ques_section_in_ratio(complexity,number_of_options):
    m=rand.randint(1,10)        #m and n are the ratio on which the line is divided
    n=rand.randint(1,10)
    return section_of_line(complexity,number_of_options,m,n)


#---------------------------------------------Main Function--------------------------------------------------#
#Main Function
if __name__=='__main__':
    complexity=int(input("Enter the complexity(1-5) : "))
    number_of_options=int(input("Enter the number of options required : "))
    complexity=complexity if complexity>0 and complexity<6 else 3
    print('_'*120)
    ques_Distance_btw_points(complexity,number_of_options)
    print('_'*120)
    ques_bisection_of_line(complexity,number_of_options)
    print('_'*120)
    ques_section_in_ratio(complexity,number_of_options)
    print('_'*120)
    ques_area_of_triangle(complexity,number_of_options)
    print('_'*120)
    ques_collinearity(complexity)
