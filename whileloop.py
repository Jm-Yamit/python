#While loop = execuse some code While Loop  some condition remains true

name = input("Enter Your Last Name: ")

while name == "":
    print("You Did Not Enter Your Name")
    name = input("Enter Your Last Name: ")

else:
    print(f"Hi {name} nice to meet you")