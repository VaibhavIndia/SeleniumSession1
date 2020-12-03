def check_even_list(numList):
    for number in numList:
        if number % 2 == 0:
            return True
        else:
            pass

print(check_even_list([1,3,7,5,2,4,6,8]))
my_new_list = [1,3,7,5,2,4,6,8]
def event_list(myList):
    list = []
    for num in myList:
        if num % 2 == 0:
            list.append(num)
        else:
            pass

    return  list
print(event_list(my_new_list))
