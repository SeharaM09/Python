#I declare that my work contains no examples of misconduct,such as plagarism,or collusion
#Any code taken from other sources is referenced within my code soluction

#W1790301

#17/04/2020

#funtion to get progress
def getProgress(pass_credit,defer_credit,fail_credit):
    credit_list = [0,20,40,60,80,100,120]
    #Check credits are in  the range 0, 20, 40, 60, 80, 100 and 120
    if pass_credit in credit_list and defer_credit in credit_list and fail_credit in credit_list:
        total= pass_credit + defer_credit + fail_credit
        #check  the total of the pass, defer and fail credits is 120
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

#Checking credit inputs are integers
try:
    pass_credit = int(input('Enter your pass credits'))
    defer_credit = int(input('Enter your defer credits'))
    fail_credit = int(input('Enter your fail credits'))
    progression= getProgress(pass_credit,defer_credit,fail_credit)
    print (progression)
    
                                                                                   
except:
    print("Integers required")

