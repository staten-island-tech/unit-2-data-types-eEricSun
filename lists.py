""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6])

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" letters = ["a","b","c","d"]
print(letters[1]) """

""" for letter in letters:
    print(letter) """

""" for letter in letters:
    if (letter == "a"):
        print("i hate you") """


""" x = "i hate children" """


""" print(x[0])
y=x.upper()
print(y) """


""" words_list = x.split(" ")
print(len(words_list)) """


""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """


""" x = "test"
print(f"hello {x}") """


""" num = int(input("type a number: "))

if (num % 2) == 0:
    print("even")
else:
    print("odd") """


""" tip = input("rate service: ")
if tip == "bad":
    print("0%")
elif tip == "okay":
    print("15%")
elif tip == "good":
    print("20%")
elif tip == "great":
    print("25%") """


""" factor = int(input("type a number: "))

print("Factors: ".format(factor))
for i in range(1, factor+1):
    if(factor % i == 0):
        print(i) """


def gcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcf = i 
    return gcf

factor1 = int(input("type a number: "))
factor2 = int(input("type a number: "))

print("Greatest Common Factor: ", gcf(factor1, factor2))

""" hunger = int(input("total hunger points: "))
x = int(input("apples eaten: "))
y = int(input("seconds passed: "))

if x > hunger:
    x = hunger

endinghunger = int(x-y)
if endinghunger < 0:
    endinghunger = 0

print((endinghunger), "hunger points left") """