import random
import random as r

lst = ["Hond","Kat","Cavia","Capybara"]
a = r.randrange(0,len(lst))
b = r.uniform(100,1000)
print(b)

def game(n):

    lst = [" "]*n+["B"]
    print(lst)
    random.shuffle(lst)
    print(lst)

    while True:
        i = input("Where do you want to check?: ")
        if lst[int(i)]=="B":
            print("You found the bomb")
            break
        else:
            print("Try again")


while True:
    try:
        a = input("Vul een getal in: ")
        b = 10/int(a)
        print(b)
        break
    except ValueError:
        print("Vul een heel getal in als nummer!")
    except ZeroDivisionError as e:

            print("Het getal mag geen nul zijn")
            print("Error : "+(e.args))

    except:
        print("Iets is verkeerd gegaan")
random.rand