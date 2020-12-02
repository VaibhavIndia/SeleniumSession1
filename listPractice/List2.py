myList = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in myList:
    print(a)
    print(b)
print(a)

name = 'vaibhav'
index_count = 0
for letter in name:
    #print("At index count  "+ index_count + letter + " is there")
    print(f"At index count  {index_count}  {letter}  is there")
    index_count += 1

new_name = ""
for x in range(len(name) - 1, -1, -1):
    new_name +=name[x]

print(new_name)

naav = input("Enter your nuame")
print(naav)
print(type(naav))