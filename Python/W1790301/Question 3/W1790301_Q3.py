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


while True:
    try:
        pass_credit = int(input('Enter your pass credits'))
        defer_credit = int(input('Enter your defer credits'))
        fail_credit = int(input('Enter your fail credits'))
        credit_list = [0,20,40,60,80,100,120]                                                                               
    
        progression= getProgress(pass_credit,defer_credit,fail_credit)
        print (progression)
        if progression == "Progress":
           progress = progress+1
        elif progression == "Progress – module trailer":
           trailing = trailing+1
        elif progression == "Exclude":
           excluded = excluded+1
        else:
           retriver = retriver+1
    except:
        print("Integers required")
         
    next_input = input("Enter q - quit the programe /or press Enter - for next student")
    if next_input=="q":
        break

list=[progress,trailing,excluded,retriver]

#finding the max value of the list
max_value=0
for j in list:
    if j>max_value:
        max_value=j
        
star_list= [[],[],[],[]]


for i in range(4):
    y=max_value-list[i]
    #append stars to stars_list
    for k in range(list[i]):
          star_list[i].append('*')
    #appending empty strings to stars_list 
    for p in range(y):
        star_list[i].append(' ')
       
print('\n')
print("progress","trailing","Exclude","retriver")
for z in range(max_value):
    print("  ",star_list[0][z],"    ", star_list[1][z],"     ", star_list[2][z],"     ",star_list[3][z])


                       
       
       
        
       
    




