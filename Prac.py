def Get_Gender(sex='unknown'):
    if sex is 'M':
        sex = "Male"
    elif sex is 'F':
        sex = "Fe(Male)"
    print(sex)


Get_Gender()
Get_Gender('M')
Get_Gender('F')

while True:
    try:
        userinput = int(input("Enter a number\n"))
        print(userinput * 5)
        break
    except ValueError:
        print("Make sure you enter a number\n")
    except ZeroDivisionError:
        break
    finally:
        print("Loop is complete")


