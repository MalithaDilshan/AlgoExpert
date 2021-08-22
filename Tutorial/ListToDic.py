
list1 = ["a", "b", "c"]
list2 = ["p", "q", "r"]

z = zip(list1, list2)
for a, b in z:
    print(a)

dic = {a: b for a, b in zip(list1, list2)}
res = dict(zip(list1, list2))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(dic))