firstname = input("Enter firstname : ")
lastname = input("Enter lastname : ")

#Concat
username = firstname + lastname
print("Username is: "+username)

email = username+"@gmail.com"
print("Email: "+email)

saved_password = "admin123"
user_password = input("Enter password")
print(saved_password==user_password)