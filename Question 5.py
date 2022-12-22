#Alphabets in reverse pyramid
a = 6
for i in range(a):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(a-i)-1):
        print(chr(65 + j), end='')
    print()
