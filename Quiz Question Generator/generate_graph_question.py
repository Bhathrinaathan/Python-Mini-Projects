import matplotlib.pyplot as plt #To plot and save the graph 
import random   #Used for generating random coordinates
from generate_Latex_Format import format_string_latex   #To format the question or options which is a string to latex
import JSON_Formatters
import json

'''
Author      : Bhathrinaathan M B
Description : Generates a question to choose a correct graph of the given points
Date        : 3rd August 2022
Last updated on : 3rd August 2022
'''

author_Name='Bhathrinaathan M B'
guid_Id='08d3ea48-d909-4d98-8c45-81d6abaceb1b'
sys_Id='Hexint09'
reveiwer_Name=''
reveiwer_Id=''

#To generate a single axis points as either x axis coordinates or y axis coordinates
def generate_axis_points(complexity):
    bound=complexity*5
    number_of_points=2 if complexity<3 else 3
    points=[random.randint(-1*bound,bound) for i in range(0,number_of_points)]
    return points


#Generates a number of options as JPEG images with random coordinates and correct answer
def generate_options(complexity,question_number,ques_x,ques_y,number_of_options):
    points=[(generate_axis_points(complexity),generate_axis_points(complexity)) for i in range(1,number_of_options)]
    points.append((ques_x,ques_y)) #Appends the question coordinates  
    random.shuffle(points)          
    options=[]
    correct_answer=0       #To denote the number of the options which is the correct answer
    for i in range(0,len(points)):
        if points[i][0] is ques_x and points[i][1] is ques_y:
            correct_answer=i+1
        plt.plot(points[i][0],points[i][1],marker='o',ms=10)
        plt.savefig(f"Q{question_number}_options_{i+1}.jpeg")
        options.append(f"/home/bhathri/HexFace/Q{question_number}_options{i+1}.jpeg")   
        #Adds the loacation of the image to options list
        plt.close()
    return correct_answer,options


#Generates a random point as question 
def generate_plot_the_points(complexity,question_number,number_of_options):
    x_axis=generate_axis_points(complexity)
    y_axis=generate_axis_points(complexity)
    plt.plot(x_axis,y_axis,marker='o',ms=10)
    plt.savefig(f"Q{question_number}_Answer.jpeg")
    plt.close()
    correct_options,options=generate_options(complexity,question_number,x_axis,y_axis,number_of_options)
    print(x_axis,y_axis)
    answer=f"/home/bhathri/HexFace/Q{question_number}_Answer.jpeg"  #Map the path of the correct answer image
    ques_str='Plot the points '
    for i in range(0,len(x_axis)):
        ques_str+=str(f'({x_axis[i]},{y_axis[i]}) ')
    ques_str+=' and choose the correct option :'
    data=JSON_Formatters.format_json_file(format_string_latex(ques_str),options,answer,author_Name,guid_Id,sys_Id,reveiwer_Name,reveiwer_Id)
    json.dumps(data)
    print(data)
    

if __name__=='__main__':
    number_of_question=int(input("Enter the number of questions required : "))
    for i in range(0,number_of_question):
        complexity=int(input("Enter the complexity (1-5) : "))
        number_of_options=int(input("Number of options required : "))
        complexity=complexity if complexity>0 and complexity<6 else 3
        generate_plot_the_points(complexity,i+1,number_of_options)
