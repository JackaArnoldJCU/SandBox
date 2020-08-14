def question():
    q = input("Do what are you converting c or f?")
    if q == 'c':
        c_to_f()
    elif q == 'f':
        f_to_c()
    else:
        question()


def c_to_f():

    c = int(input("What is your Celsius:"))
    print(c*1.8+32)


def f_to_c():

    f = int(input("What is your Fahrenheit:"))
    print((f-32)/1.8)


question()