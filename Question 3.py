#Printing the input number and its square
Numbers = map(int,input("Enter numbers separated by a space:").split())
List=[]                 #Create an empty list
for i in Numbers:
    Tupple =(i,i**2)
    List.append(Tupple)      #Add Tupple to the list
print("The list of numbers and its square is:\n",List)
