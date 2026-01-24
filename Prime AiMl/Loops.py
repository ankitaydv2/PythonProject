age = int(input("Enter age : "))
if(age >= 18):
    print("you are eligible to fill the form")
else:
    print("you don't have the access ")

# Traffic Lights
color = input("Enter the color : ")
if(color == "red"):
    print("Stop")
elif(color == "green"):
    print("Go")
elif(color == "Orange"):
    print("Wait and Go")
else:
    print("Wrong color given ")

#3 Usename & Password
Username = input("Enter username : ")
password = input("Enter password : ")
if(Username == "admin" and password == "hellow@123"):
    print("You successfully logged in! ")
elif(Username == "admin" and password != "hellow@123"):
    print("Password is wrong, Please try again.")
elif(Username != "admin" and password == "hellow@123"):
    print("Username is wrong, Please try again.")
else:
    print("Wrong username or password.")

#4 If n is multiple of 5 or not
n = int(input("Enter n : "))
for i in range(1, 11):
    print(n*i)

#5 Print Odd or Even
n = int(input("Enter number : "))
if(n % 2 == 0):
    print("n is Even.")
else:
    print("n is Odd.")
