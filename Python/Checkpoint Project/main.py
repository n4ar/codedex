print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

choice = int(input("Which shape? : "))

if choice == 1:
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = (height * base) / 2
    print(f"Area of triangle: {area:.2f}")
elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of rectangle: {area:.2f}")
elif choice == 3:
    side = float(input("Enter side length: "))
    area = side ** 2
    print(f"Area of square: {area:.2f}")
elif choice == 4:
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius ** 2
    print(f"Area of circle: {area:.2f}")
elif choice == 5:
    print("Exiting...")
else:
    print("Invalid choice")
