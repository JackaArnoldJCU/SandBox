def main():
    password = input("Password:")
    password_checker(password)
    print("*"*len(password))



def password_checker(password):
    if len(password) <= 0:
        print("Too Short")
        main()

main()