#-----------------------------------------------------------------------------------
marks = int(input("enter the marks of the student"))

if (marks>=90):
    print("The grades is A")
elif (marks>80 and marks <90):
    print("The grade is B")
elif (marks>70):
    print("The grade is C")
else :
    print("the studens has failed the exam")

#-----------------------------------------------------------------------------------

num = int(input("enter the number"))

if (num%2==0):
    print ("it is a even number")
    
else:
    print ("it is a odd number")

#-------------------------------------------------------------------------------------

num1 = int(input("enter the number 1")) 

num2 = int(input("enter the number 2"))

num3 = int(input("enter the number 3"))

if (num1>num2 and num1>num3):
    print (num1)

elif (num2>num1 and num2>num3):
    print (num2)
    
else:
    print(num3)
    
#---------------------------------------------------------------------------------------

