#Fibonacci Sequence
terms = int(input("Enter number of terms for the sequence :"))
n1 = 0
n2 = 1
Sum=0
if terms<=0:
    print("Please enter a positive integer")
elif terms==1:
    print(f"Fibonacci Sequence up to {terms} term :\n{n1}\nAverage of the Series = 0")
else:
    print(f"Fibonacci Sequence up to {terms} terms :")
    for i in range(terms):                     #We use a loop to keep adding the terms again and again until no of terms is reached
        print(n1)
        Sum += n1
        nx=n1 + n2
        n1=n2
        n2=nx
    Average = Sum/terms
    print(f"The average of the series = {Average}")
