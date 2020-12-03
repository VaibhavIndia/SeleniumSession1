for num in range(0,10):
    if num % 2 == 0:
        print(num)
    else:
        continue

myList = []
for num in range(1,50):
    if num % 3 == 0:
        myList.append(num)
    else:
        continue

print(myList)

for num in range (1,100):
    if num % 3 == 0 and num % 5 == 0:
        print(f" {num} FIZZBUZZ")
    elif num % 3 == 0 and num % 5 != 0:
        print(f"{num} Fizz")
    elif num % 3 != 0 and num % 5 ==0:
        print(f"{num} BUZZ")
    else:
        print(num)

#print(help(myList.append))
def hello():
    '''
    my docs
    '''
    print("hello")
    print("buddy")

hello()
hello()
