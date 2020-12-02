from random import shuffle

mynumList = [num**2 for num in range(1,11)]
print(mynumList)
#shuffle(mynumList)
#print(mynumList)

mynewList = [x if X%2==0 else "ODD" for x in range(1,11) ]
print(mynewList)