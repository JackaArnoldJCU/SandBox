def get_password():
    password = input("Password:")
    password_checker()
    print("*"*len(password))

def password_checker():
    global password
    if len(password) <= 0:
        print("Too Short")
        main()





get_password()