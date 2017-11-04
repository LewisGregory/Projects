print("welcome to my area Calculator")
print("1 circle O")
print("2 square/rectangle []")
print("3 triangle ^")
shape = input("please enter you desired shape") 
#here i check if the user has chosen a circle
if shape == "1":
    di = input("what is the circles diameter: ")
    #here i setup the variables of pi and the diameter which are needed to calculate the area
    pi = 3.14
    #here i use these variable to calculate the area of the circle
    area = pi*(int(di))
    print("the area of your circle is: " + str(area))
    
#here i check if the user has chosen a square/rectangle 
elif shape == "2":
    h = int(input("what is the height of the square/rectangle "))
    w = int(input("what is the width of the sqaure/rectangle"))
    #here i setup the variables of the height and width
    area = h*w
    #here i use the variables to calculate the area
    print("the are of your square/rectangle is: " + str(area))
#i check to see if the user has chosen a triangle
elif shape == "3":
    
    h = int(input("what is the height of the triangle "))
    #here i am setting up the variables height and whidth
    w = int(input("what is the width of the triangle"))
    #i then calculate the area of the challenge
    area = (h*w)/2 
    print("the area of your triangle is: " + str(area))
