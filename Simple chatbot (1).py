def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    r1=int(input())
    r2=int(input())
    r3=int(input())
    age=((r1 * 70) + (r2 * 21) + (r3 * 15)) % 105
    print("Your age is :",age," that's a good time to start programming!")
    
def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("Which one of the following is not a predefined data types data type?")
    print("1. List")
    print("2. Class")
    print("3. Dictionary")
    print("4. Tuple")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('Completed!')
    print('.................................')

def end():
    print('Congratulations, have a nice day!')
    print('.................................')

    
greet('Pybot', '2021') 
remind_name()
guess_age()
count()
test()
while(True):
    t=input("Do you want to repeat any task? y/n")
    if t=="y":
        r=input("Which task do you want to repeat?\n 1.guess_age \n 2.count \n 3.test")
        if r=="1":
            guess_age()
        if r=="2":
            count()
        if r=="3":
            test()
    
    else:
        break
        
            

while(True):
    x=input("Do you want to continue from the start? y/n")
    if x=="y":
        greet('Pybot', '2021')
        remind_name()
        guess_age()
        count()
        test()
    else:
        end()
        break
    









