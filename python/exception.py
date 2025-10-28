try:
    a = int(input("tell your age"))
    print(45/a)
except Exception as err:                      #ZeroDivisionError:
    print(f"Sorry there is an error {err}")
else:
    print("good there is no exception")
finally:
    print("i will run no matter what")

# raise - manually throws an exception

age = int(input("tell me your age"))
try:
    if age < 10 or age > 18:
        raise ValueError("your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"an error occurred as {err}")

    
