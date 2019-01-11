# 1) if an error occured:
   # try > except > finaly

# 2) if no error:
    # try > else > finally

# if there are such constructions like continue or break -- finally block will execute before them no matter what

def ask_for_int():

    while True:
        try:
            num = int(input("Enter a number: "))
            # manualy throw
            raise NameError

        except ValueError:
            print("Whoops, you entered a wrong integer\n")
            continue
        except NameError:
            pass
        else:
            print("else")
            break
        finally:
            print("Finaly\n")



# ask_for_int()


for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Unsupported type\n")



x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by zero\n")
finally:
    print("All done\n")


while True:
    try:
        num = int(input("Input an integer: "))
        squared = num * num
    except ValueError:
        print("An error occurred! Please try again!")
        continue
    else:
        print(f"Thank you, your number squared is: {squared}")
        break