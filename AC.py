print("welcome to my area Calculator")
print("1 circle O")
print("2 square/rectangle []")
print("3 triangle ^")
shape = input("please enter you desired shape") 
if shape == "1":
    di = input("what is the circles diameter: ")
    pi = 3.14
    area = pi*(int(di))
    print("the area of your circle is: " + str(area))
elif shape == "2":
    h = int(input("what is the height of the square/rectangle "))
    w = int(input("what is the width of the sqaure/rectangle"))
    area = h*w
    print("the are of your square/rectangle is: " + str(area))
elif shape == "3":
    h = int(input("what is the height of the triangle "))
    w = int(input("what is the width of the triangle"))
    area = (h*w)/2
    print("the area of your triangle is: " + str(area))
