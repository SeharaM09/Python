#I declare that my work contains no examples of misconduct,such as plagarism,or collusion
#Any code taken from other sources is referenced within my code soluction

#W1790301

#17/04/2020
#function to get progress

def getProgress(pass_credit,defer_credit,fail_credit):
    credit_list = [0,20,40,60,80,100,120]
    if pass_credit in credit_list and defer_credit in credit_list and fail_credit in credit_list:
        total= pass_credit + defer_credit + fail_credit
        if total==120:
            if pass_credit==120:
               output= "Progress"
            elif pass_credit==100:
               output= "Progress – module trailer"
            elif fail_credit>=80:
               output= "Exclude"
            else:
               output= "Do not progress – module retriever"               
        else:
            output='Total incorrect'
            
    else:
        output= "Range Error"
   
    return output

progress = 0
trailing = 0
retriver = 0
excluded = 0

#create a list for access the data

credit_list=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]
for i in credit_list:   
    try:                                                                          
        progression= getProgress(i[0],i[1],i[2])
        print (progression)
        if progression == "Progress":
           progress = progress+1
        elif progression == "Progress – module trailer":
           trailing = trailing+1
        elif progression == "Exclude":
           excluded = excluded+1
        elif progression == "Do not progress – module retriever":
           retriver = retriver+1
    except:
        print("Integers required")
         
    

print (f"Progress {progress}   : {progress*'*'}")
print (f"Trailing {trailing}   : {trailing*'*'}")
print (f"Retriver {retriver}   : {retriver*'*'}")
print (f"Excluded {excluded}   : {excluded*'*'}")


                       
       
       
        
       
    




