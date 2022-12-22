Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
Set1_10 = set(range(1,11))

#(a)Elements that are in Set1 and Set2 but not both
a = Set1^Set2
print("Elements that are in Set1 and Set2 but not both are :",a)

#(b)Elements that are in only one of the three sets Set1,Set2 and Set3
b = Set1^Set2^Set3
print("\nElements that are in only one of the three sets Set1,Set2 and Set3 are :",b)

#(c)Elements that are exactly two of the sets Set1, Set2 and Set3
c = Set1&Set2 | Set2&Set3 | Set1&Set3
print("\nElements that are exactly two of the sets Set1, Set2 and Set3 are :",c)

#(d)Set of all integers in the range 1 to 10 that are not in Set1
d = Set1_10 - Set1
print("\nSet of all integers in the range 1 to 10 that are not in Set1 are :",d)

#(e)Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3
e = Set1_10 - Set1 - Set2 - Set3
print("\nSet of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 are :",e)
