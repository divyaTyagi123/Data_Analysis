"""# 1
num = 34535
while num>0 : 
    print(num%10 , end = "")
    num = num//10


# 2
print()
num2 = 35356345

num3 =0
while num2>0:
    num3 = num3 * 10 + num2%10
    num2 = num2//10

print(num3)
while num3>0:
    print(num3 % 10)
    num3 = num3//10


#3  Random number
import random
number = random.randint(1,10)


chances = 0
while chances<3:
    guess = int(input("Enter your guessed number"))
    if guess == number:
        print("You won")
        break
    else:
        print("Bad choice ! Try Again")
        chances += 1
    4
if chances == 3:
    print("Sorry ! You loose")

    """
