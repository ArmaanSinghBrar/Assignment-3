#Number of occurrences of words or alphabets
List=input("Enter a string").split()
if len(List)>1:
    for i in set(List):
        Count=List.count(i)
        print(f"Word {i} occurs {Count} times")
elif len(List)==1:
    word=List[0]
    for i in set(word):
       Count=word.count(i)
       print(f"Alphabet {i} occurs {Count} times")
