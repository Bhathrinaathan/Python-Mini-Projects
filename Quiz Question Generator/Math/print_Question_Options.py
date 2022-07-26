def print_Ques_Opt_Ans(terms,options,number_of_options,answer,operator):
    print("Select the correct option for the following multiplication : ")
    for term in terms[0:-1]:
        print(term," ",operator,end=" ")
    print(terms[-1],"  = ")
    print("The options are given below : ")
    for i in range(0,number_of_options):
        print('\t',"(",(i+1),")",options[i])
    print('\n','Correct Answer : ','(',options.index(answer)+1,')',answer,'\n')
