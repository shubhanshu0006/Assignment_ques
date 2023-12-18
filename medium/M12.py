password = "hello"
t = 3
print("Enter username")
user_name = input()
print("Enter Password")

for i in range(3):
    user_password = input()
    if user_password == password:
        print("Correct Password")
        break
    

    else:
        if i ==2:
            print("wrong password")
        else:
            print("wrong password")
            print("Enter Again")


        
       
