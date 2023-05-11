print("[1] REGISTER")
print("[2] AUTENTICATION")
print("[3] LOGOFF")

option = int(input("Digite uma opção: "))

if (option == 1):
    name = input("Digite o seu nome: ")
    phone_number = int(input("Digite a sua idade: "))
    email = input("Digite o seu e-mail: ")
    
    print("--------------------")
    print("Name: %s" %name)
    print("E-mail: %s" %email)
    print("Phone number: %d" %phone_number)
    print("Successfully registered user!")
    print("--------------------")
    
elif (option == 2):
    
    email = input("Digite o seu e-mail: ")
    password = input("Digite a sua senha: ")
    
    email_user = "admin@email.com"
    password_user = "123456"
    
    print("--------------------")
    print("E-mail: %s" %email)
    print("Password: *******")
    
    if (email_user == email) and (password_user == password):
        print("Successyfully authenticated user!")
    else:
        print("Incorrect password. Try again!")
    

elif (option == 3):
    print("Do you want to exit the system? Y - YES | N - NO")
    answer = input("Do you really want to disconnect?__")
    
    if (answer == "Y"):
        print("Disconnecting user...")
    else:
        print("User is logged in...")

else: 
    print("Enter a valid option!")
