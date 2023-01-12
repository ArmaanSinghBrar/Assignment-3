#Alphabets in reverse pyramid
Rows = 6
for i in range(Rows):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(Rows-i)-1):
        print(chr(65 + j), end="")
    print()
