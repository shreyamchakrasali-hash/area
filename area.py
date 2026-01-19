import math

def area_circumference(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return f"Area:{area}, Circumference:{circumference}"

if __name__ == "__main__":
    print(area_circumference(5))
