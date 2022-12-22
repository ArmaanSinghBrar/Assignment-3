#Creating a Tuple with a input number and its square
number = map(int,input("Enter numbers separated by a space:").split())
Tuple = []        #an empty list
for i in number:
    num2 = (i,i**2)
    Tuple.append(num2)    #we add the values to emplty list to make a tuple
print("The tuple with input number and it's square is:\n",Tuple)
