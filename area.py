import math
def area_cicumference(radius):
    area=math.pi*radius*radius
    circumference=2*math.pi*radius
    result=(
        f"Area: {area}",
        f"Circumference: {circumference}"
    )

if __name__ == "__main__":
    print(area_cicumference(5))
