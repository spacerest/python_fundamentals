'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''




#method one

unsorted_list = [('first_element', 40000), ('second_element', 2000), ('third_element', 166)]
sorted_list = []



#while we still have values in the unsorted list
while len(unsorted_list) > 0:
    #loop through the unsorted list to find the minimum value
    min_value = unsorted_list[0][1]
    index = 0
    for tuple_ in unsorted_list:
        #save the minimum value to use outside of this for loop
        if tuple_[1] <= min_value:
            min_value = tuple_[1]
            min_index = index
        index += 1

    #push the minimum value onto the sorted list
    sorted_list.append(unsorted_list.pop(min_index))
    print("unsorted list is " + str(unsorted_list))

print(sorted_list)

#method two
unsorted_list = [('first_element', -40000), ('second_element', 2000), ('third_element', 166)]
sorted_list = []

value_list = []
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)
value_list.sort()

for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
            break

print(sorted_list)



print("end of sadies")


#method 3

for x in range(0, len(unsorted_list)):

    current_min = unsorted_list[0][1]
    print(current_min)
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])


print(unsorted_list)
print(sorted_list)


#method 3

unsorted_list = [('first_element', 40000), ('second_element', 2000), ('third_element', 166)]
sorted_list = []
for tup in list(unsorted_list):

    current_min = unsorted_list[0][1]
    index = 0

    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])

print("caycay")
print(unsorted_list)
print(sorted_list)
print("------------")




# method 4
unsorted_list = [('first_element', 40000), ('second_element', 2000), ('third_element', 166)]
sorted_list = []

sorted_list = sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)