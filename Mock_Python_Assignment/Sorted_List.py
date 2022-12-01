n=int(input("Enter number of elements: "))
lst=[]
for i in range(n):
    element=input("Enter element: ")
    lst.append(element)

first_element=lst[0]
lst.pop(0) #remove first element of a list

lst.sort()
sorted_Second_list=[]
sorted_Second_list.append(first_element)
for i in range(n-1):
    sorted_Second_list.append(lst[i])


print(sorted_Second_list)
