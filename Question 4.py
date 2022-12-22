grade_point = int(input("Enter your Grade Point in the range[4-10] :"))
if(grade_point==10):
    print("Your Grade is ‘A+’ and Outstanding Performance.")
elif(grade_point==9):
    print("Your Grade is ‘A’ and Excellent Performance.")
elif(grade_point==8):
    print("Your Grade is ‘B+’ and Very Good Performance.")
elif(grade_point==7):
    print("Your Grade is ‘B’ and Good Performance.")
elif(grade_point==6):
    print("Your Grade is ‘C+’ and Average Performance.")
elif(grade_point==5):
    print("Your Grade is ‘C’ and Below Average Performance.")
elif(grade_point==4):
    print("Your Grade is ‘D’ and Poor Performance.")
else:
    print("Error\nPlease enter a valid Grade Point in the range[4,10]")
    
    
    
#Another method of solving the question
grade_point = int(input("Enter your Grade Point in the range[4-10] :"))
a = {10:"Your Grade is ‘A+’ and Outstanding Performance.",    #giving grade and performance to each grade point
         9:"Your Grade is ‘A’ and Excellent Performance.",
         8:"Your Grade is ‘B+’ and Very Good Performance.",
         7:"Your Grade is ‘B’ and Good Performance.",
         6:"Your Grade is ‘C+’ and Average Performance.",
         5:"Your Grade is ‘C’ and Below Average Performance.",
         4:"Your Grade is ‘D’ and Poor Performance."}
grade = a.get(grade_point)      #grade is the grade and performance for the entered grade point
if (4<=grade_point<=10):
    print(grade)
else:
    print("Error\nPlease enter a valid Grade Point in the range[4,10]")
