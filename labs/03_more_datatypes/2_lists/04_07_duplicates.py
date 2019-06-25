'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

print(set(list_))

unique = []
for i in list_:
    if i not in unique:
        unique.append(i)

print(unique)


list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print(max(list1))
print(max(list2))