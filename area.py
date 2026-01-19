def area_circumference(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return (
        f"Area : {area}",
        f"Circumference : {circumference}"
    )

if __name__ == "__main__":
    radius = 5
    result = area_circumference(radius)

    for value in result:
        print(value)
