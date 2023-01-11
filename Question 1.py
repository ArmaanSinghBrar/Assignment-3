#Number of occurrences of words or alphabets
List=input("Enter a string").split()
if len(List)>1:                #if the string is a sentence
    for i in set(List):        #running a loop for all words in the string
        Count=List.count(i)
        print(f"Word {i} occurs {Count} times")
elif len(List)==1:              #If the string is a word
    word=List[0]
    for i in set(word):         #running a loop for all alphabets in the word
       Count=word.count(i)
       print(f"Alphabet {i} occurs {Count} times")
