#Word or letter count in string
string = str(input("Enter the string:"))
list1 = string.split()
list_l = []
for e in list1:
    lower_e = e.lower()
    list_l.append(lower_e)
set1 = set(list_l)
dic = {}
for el in set1:
    count = list_l.count(el)
    dic.update({el: count})
list2 = []
dic2 = {}
set2 = {1, 2}
set2.clear()
if len(list1) == 1:

    for elements in string:
        list2.append(elements)

    for el in list2:
        set2.add(el.lower())

    string_l = string.lower()
    for elem in set2:
        dic2.update({elem: string_l.count(elem)})

    print("Letter count is :")
    print(dic2)

else:
    print("The Word Count is :")
    print(dic)
