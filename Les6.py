def som(lijst):
    totaal = 0#accumulator
    for num in lijst:

        totaal+=num
    return totaal
def acronym(phrase):
    lst = phrase.split()
    s = "" #accumulator
    for word in lst:
        s+= word[0]
    return s.upper()
def nested(n):

    for j in range(n):
        for i in range(n):
            print(i,end =" ")
        print()

def print2DTable(table):
    for rij in table:
        for item in rij:
            print(item)

def pixels(table):
    totaal = 0
    for rij in table:
        for item in rij:
            if item>0:
                totaal+=1
            elif item<0:
                print("Hey vul een positieve pixel in")

    return totaal

def eigen_forloop(lst):
    i =0
    while i<len(lst):

        print(f"{i}, {lst[i]}" )
        i += 1


optellen()