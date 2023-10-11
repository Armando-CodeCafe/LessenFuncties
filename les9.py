import random
def game(n):
    'a simple bomb finding game'


    table =[" "]* n + ["B"]
    print(table)
    random.shuffle(table)
    print(table)
    while True:
        pos = input('Enter next position: ')

        if table[int(pos)]== 'B':
            print('You found the bomb!')
            break
        else:
            print('No bomb at position', pos)

while True:
    try:
        a = input("Age: ")
        b = 10/int(a)
        print(b)
        break
    except ZeroDivisionError:
        print("Je hebt door 0 gedeeld")
    except ValueError as e:
        pass