x = input("Enter the shape: ")
def Area(x):
    if x == "Triangle" or x == "":
        try:
            base = int(input("Enter the base of the triangle: "))
        except Exception as e:
            print("ValueError")
            base = None
        try:
            height = int(input("Enter the height of the triangle: "))
        except Exception as e:
            print("ValueError")
            height = None
        try:
            area = (1/2)*base*height
        except Exception as e:
            print('TypeError')
            area = None
        print("Area of the triangle is ",area)

    elif x == "Rectangle":
        try:
            height = int(input("Enter the height: "))
        except Exception as e:
            print("ValueError")
        try:
            width = int(input("Enter the width: "))
        except Exception as e:
            print("TypeError")
        try:
            area = height * width
        except Exception as e:
            print("ValueError")
            area = None
        print("Area of the rectangle is ",area)


Area(x)