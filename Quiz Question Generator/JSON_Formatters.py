'''
Author      : Bhathrinaatha M B
Description : Formats a given string,options which are in latex format into a dictionary 
              as JSON format
Date        : 27th July 2022
Last Updated on :  29th July 2022
'''

def format_json_file(question,options,answer,author,guidId,sysId,reveiwerName,reveiwerId):
    data={}
    data['question']=question
    data['answers']=[]
    data['Author']={'Name':author,'GUID_ID':guidId,'System_ID':sysId,'Reviwer_Name':reveiwerName,'Reviewer_ID':reveiwerId};
    for i in range(0,len(options)):
        answer={}
        answer['ID']=i+1
        answer['content']=options[i]
        answer['key']=0 if answer['content']!=answer else 1
        data["answers"].append(str(answer))
    return str(data)
