inputName = input("Input your name\n")

name = inputName.split(' ')
ini = ""

for x in name:
 ini += list(x)[0]
 
print("Initials: " + ini + "\n")
print(inputName + ", welcome to python programming!")




